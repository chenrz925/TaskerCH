# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.
from sys import argv as sys_argv

from ._launcher import Launcher

if __name__ == '__main__':
    launcher = Launcher(*sys_argv[1:])
    launcher()
