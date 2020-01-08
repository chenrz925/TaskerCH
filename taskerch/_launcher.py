from typing import Text

from taskerch.task import Namespace
from toml import load as toml_load


class Launcher(object):
    def _parse_config(self, path: Text) -> Namespace:
        return Namespace(toml_load(path))

    def __init__(self, path: Text):
        self._config = self._parse_config(path)

