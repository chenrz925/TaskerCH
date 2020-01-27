# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.
from abc import ABCMeta, abstractmethod

from box import Box


class Shared(Box, metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        raise NotImplementedError

    @abstractmethod
    def dump(self):
        raise NotImplementedError
