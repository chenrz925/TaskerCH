# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.

from typing import Any, Text, Dict, Tuple, List

from ._dependency import Box, UUID
from ._dependency import toml_load, product
from .exception import LinkValueTypeMismatchError, TomlNotFoundError, GridSearchValueTypeMismatchError


class Configuration(Box):
    def __init__(self, raw_dict: Dict[Text, Any], mutable=False, **kwargs):
        kwargs['frozen_box'] = not mutable
        kwargs['default_box'] = True
        kwargs['camel_killer_box'] = True
        super(Configuration, self).__init__(
            raw_dict,
            **kwargs,
        )


class ConfigurationCreator:
    def __init__(self, path: Text):
        self._raw_dict = toml_load(path)

    @staticmethod
    def _parse_link(node: Dict[Text, Any]) -> Dict[Text, Any]:
        def parse_elem(value: Any) -> Any:
            if isinstance(value, List):
                return list(map(
                    parse_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return dict(map(
                    parse_node,
                    value,
                ))
            else:
                return value

        def parse_node(key: Text, value: Any) -> Tuple[Text, Any]:
            if key.startswith('@'):
                if isinstance(value, Text):
                    try:
                        link_value = toml_load(value)
                        return key[1:], link_value
                    except FileNotFoundError:
                        raise TomlNotFoundError(value)
                else:
                    raise LinkValueTypeMismatchError(key, type(value))
            elif isinstance(value, List):
                return key, list(map(
                    parse_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return key, dict(map(
                    lambda kv: parse_node(*kv),
                    value.items(),
                ))
            else:
                return key, value

        return dict(map(
            lambda kv: parse_node(*kv),
            node.items(),
        ))

    @staticmethod
    def _parse_grid(node: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        grid_search_value_mappings = {}
        grid_search_key_mappings = {}

        def parse_elem(value: Any) -> Any:
            if isinstance(value, List):
                return list(map(
                    parse_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return dict(map(
                    parse_node,
                    value,
                ))
            else:
                return value

        def parse_node(key: Text, value: Any) -> Tuple[Text, Any]:
            if key.startswith('#'):
                if isinstance(value, List):
                    uuid = UUID().hex
                    grid_search_key_mappings[uuid] = key
                    grid_search_value_mappings[uuid] = value
                    return uuid, None
                else:
                    raise GridSearchValueTypeMismatchError(key, type(value))
            elif isinstance(value, List):
                return key, list(map(
                    parse_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return key, dict(map(
                    lambda kv: parse_node(*kv),
                    value.items(),
                ))
            else:
                return key, value

        mapped_node = dict(map(
            lambda kv: parse_node(*kv),
            node.items(),
        ))
        grid_products = list(map(
            lambda v: dict(zip(grid_search_value_mappings, v)),
            product(*grid_search_value_mappings.values()),
        ))

        def fill_elem(value: Any) -> Any:
            if isinstance(value, List):
                return list(map(
                    fill_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return dict(map(
                    fill_node,
                    value,
                ))
            else:
                return value

        def fill_node(fill: Dict[Text, Any], key: Text, value: Any) -> Tuple[Text, Any]:
            if key in fill:
                return (grid_search_key_mappings[key][1:], fill[key])
            elif isinstance(value, List):
                return key, list(map(
                    fill_elem,
                    value,
                ))
            elif isinstance(value, Dict):
                return key, dict(map(
                    lambda kv: fill_node(fill, *kv),
                    value.items(),
                ))
            else:
                return key, value

        return list(map(
            lambda fill: dict(map(
                lambda kv: fill_node(fill, *kv),
                mapped_node.items(),
            )),
            grid_products,
        ))

    def create(self) -> List[Configuration]:
        return list(map(
            lambda raw: Configuration(raw),
            self._parse_grid(self._parse_link(self._raw_dict))
        ))
