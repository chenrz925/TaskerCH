# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.

from uuid import uuid4 as UUID
from itertools import product

from colorama import Fore, Back, Style, init as _colorama_init
_colorama_init(
    autoreset=True
)
from box import Box
from toml import load as toml_load

from taskerch._config import ConfigurationCreator, Configuration

__version__ = '0.0.2'
