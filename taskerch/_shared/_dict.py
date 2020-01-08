from typing import NoReturn, Text, Any

from taskerch._shared import Shared


class DictShared(Shared):
    def __init__(self, *args, **kwargs):
        self._values = {}

    def __getitem__(self, key: Text) -> Any:
        return self._values.__getitem__(key)

    def __setitem__(self, key: Text, value: Any) -> NoReturn:
        self._values.__setitem__(key, value)

    def __delitem__(self, key: Text) -> NoReturn:
        self._values.__delitem__(key)

    def sync(self) -> NoReturn:
        pass

    def clean(self) -> NoReturn:
        pass
