from abc import ABCMeta, abstractmethod
from typing import Dict, Text, Any
import taskerch._const as const


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


class Task(metaclass=ABCMeta):
    """
    The fundamental unit to execute. You don't need to modify the `__init__` function and all configurations in TOML will be inject into `self.config`.
    """

    def __init__(self, config: Dict[Text, Any], shared: Dict[Text, Any]):
        """

        :param config:
        :param shared:
        """
        self.__dict__.update(config)
        super(Task, self).__setattr__('_shared', shared)

    @property
    def shared(self) -> Dict[Text, Any]:
        return self._shared

    def __setattr__(self, key, value):
        if key == '_shared':
            raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)
        else:
            super(Task, self).__setattr__(key, value)

    def __delattr__(self, item):
        if item == '_shared':
            raise RuntimeError(const.ERROR_OPERATION_NOT_ALLOWED)
        else:
            super(Task, self).__delattr__(item)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


if __name__ == '__main__':
    pass
