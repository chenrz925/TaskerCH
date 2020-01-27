# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.
from typing import Text, Type

from ._dependency import Back, Fore, Style


class TomlNotFoundError(RuntimeError):
    def __init__(self, path: Text):
        super(TomlNotFoundError, self).__init__(
            f'TOML file {Back.RED}{Fore.WHITE}"{path}"{Style.RESET_ALL} does NOT exist.'
        )


class LinkValueTypeMismatchError(RuntimeError):
    def __init__(self, attribute: Text, value_type: Type):
        super(LinkValueTypeMismatchError, self).__init__(
            f'TOML attribute {Back.WHITE}{Fore.RED}"{attribute}"{Style.RESET_ALL} of type {Back.RED}{Fore.WHITE}"{value_type.__name__}"{Style.RESET_ALL} mismatches to needed type "{str.__name__}".'
        )


class GridSearchValueTypeMismatchError(RuntimeError):
    def __init__(self, attribute: Text, value_type: Type):
        super(GridSearchValueTypeMismatchError, self).__init__(
            f'TOML attribute {Back.WHITE}{Fore.RED}"{attribute}"{Style.RESET_ALL} of type {Back.RED}{Fore.WHITE}"{value_type.__name__}"{Style.RESET_ALL} mismatches to needed type "{list.__name__}".'
        )
