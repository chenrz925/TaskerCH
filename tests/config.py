import unittest
from sys import stderr

from taskerch._config import ConfigurationCreator
from taskerch.exception import TomlNotFoundError, LinkValueTypeMismatchError


class ConfigurationCase(unittest.TestCase):
    def test_config_link(self):
        creator = ConfigurationCreator('config/test-main.toml')
        print(creator._parse_link(creator._raw_dict), file=stderr)

    def test_exception_1(self):
        try:
            creator = ConfigurationCreator('config/test-exception-1.toml')
            print(creator._parse_link(creator._raw_dict), file=stderr)
        except Exception as e:
            self.assertIsInstance(e, TomlNotFoundError)

    def test_exception_2(self):
        try:
            creator = ConfigurationCreator('config/test-exception-2.toml')
            print(creator._parse_link(creator._raw_dict), file=stderr)
        except Exception as e:
            self.assertIsInstance(e, LinkValueTypeMismatchError)

    def test_config_grid(self):
        creator = ConfigurationCreator('config/test-main-grid.toml')
        print(creator._parse_grid(creator._raw_dict), file=stderr)

    def test_config_create(self):
        creator = ConfigurationCreator('config/test-main-grid.toml')
        configs = creator.create()
        print(configs)

if __name__ == '__main__':
    unittest.main()
