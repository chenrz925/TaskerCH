from abc import ABCMeta, abstractmethod
from typing import Text, Any, NoReturn


class Shared(metaclass=ABCMeta):
    @abstractmethod
    def __getitem__(self, key: Text) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def __setitem__(self, key: Text, value: Any) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def __delitem__(self, key: Text) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def sync(self) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def clean(self) -> NoReturn:
        raise NotImplementedError()
