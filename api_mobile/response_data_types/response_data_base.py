from abc import ABC, abstractmethod

from utils.methods import obj_to_string
from unittest import TestCase


class BaseType(ABC):

    def __init__(self):
        self._tc = TestCase()

    def __str__(self):
        return obj_to_string(self)

    def dict(self):
        data = {}
        for key in self.__dict__.keys():
            if not key.startswith("_"):
                data[key] = getattr(self, key)
        return data

    @abstractmethod
    def check(self, client, **kwargs):
        pass


class BaseTypeParent(BaseType, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_data_to(self, obj):
        pass
