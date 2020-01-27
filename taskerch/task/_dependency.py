# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.
from abc import ABCMeta, abstractmethod
from collections import Callable
from logging import Logger

from taskerch._config import Configuration
from taskerch._shared import Shared


class Task(Callable, metaclass=ABCMeta):
    def __init__(self, logger: Logger, shared: Shared, config: Configuration):
        self.logger = logger
        self.shared = shared
        self.config = config

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
