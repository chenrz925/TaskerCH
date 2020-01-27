# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.

import unittest
from sys import stderr

from taskerch.exception import TomlNotFoundError, LinkValueTypeMismatchError


class ExceptionCase(unittest.TestCase):
    def test_toml_not_found(self):
        try:
            raise TomlNotFoundError('PATH')
        except TomlNotFoundError as e:
            print(e, file=stderr)
            self.assertIsInstance(e, TomlNotFoundError)

    def test_link_type_mismatch(self):
        try:
            raise LinkValueTypeMismatchError('ATTRIBUTE', object)
        except LinkValueTypeMismatchError as e:
            print(e, file=stderr)
            self.assertIsInstance(e, LinkValueTypeMismatchError)


if __name__ == '__main__':
    unittest.main()
