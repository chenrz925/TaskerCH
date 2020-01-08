from abc import ABCMeta, abstractmethod
from typing import Dict, Text, Any, NoReturn

import taskerch._const as const
from taskerch._shared import Shared


class Namespace:
    def __init__(self, value: Dict[Text, Any]):
        self.__dict__.update(filter(
            lambda item: not isinstance(item[1], list) and not isinstance(item[1], dict),
            value.items()))
        self.__dict__.update(map(
            lambda item: (item[0], Namespace(item[1])),
            filter(
                lambda item: isinstance(item[1], dict),
                value.items()
            )))
        self.__dict__.update(map(
            lambda item: (item[0], list(map(
                lambda elem: Namespace(elem) if isinstance(elem, dict) else elem,
                item[1],
            ))),
            filter(
                lambda item: isinstance(item[1], list),
                value.items()
            )))

    def __getitem__(self, key: Text):
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, value):
        raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    def __setattr__(self, key, value):
        raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    def __delitem__(self, key):
        raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    def __delattr__(self, item):
        raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    @property
    def dict(self):
        return self.__dict__


class Task(metaclass=ABCMeta):
    """
    The fundamental unit to execute. You don't need to modify the `__init__` function and all configurations in TOML will be inject into `self.config`.
    """

    def __init__(self, config: Namespace, shared: Shared):
        """

        :param config:
        :param shared:
        """
        super(Task, self).__setattr__('_config', config)
        super(Task, self).__setattr__('_shared', shared)

    @property
    def config(self) -> Namespace:
        return super(Task, self).__getattribute__('_config')

    @property
    def shared(self) -> Shared:
        return super(Task, self).__getattribute__('_shared')

    def __getattribute__(self, key: Text) -> Any:
        if key not in ['_config', '_shared']:
            return super(Task, self).__getattribute__(key)
        else:
            raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    def __setattr__(self, key: Text, value: Any) -> NoReturn:
        if key not in ['_config', '_shared']:
            super(Task, self).__setattr__(key, value)
        else:
            raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    def __delitem__(self, key: Text) -> NoReturn:
        if key not in ['_config', '_shared']:
            super(Task, self).__delattr__(key)
        else:
            raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


if __name__ == '__main__':
    pass
