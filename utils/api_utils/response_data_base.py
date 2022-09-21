from abc import ABC, abstractmethod

from utils.methods import obj_to_string
from unittest import TestCase


class BaseType(ABC):

    def __init__(self):
        self._tc = TestCase()

    def __str__(self):
        return obj_to_string(self)

    def to_dict(self):
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

    @staticmethod
    def deserialize_to_list_of(type_name: type, data: list):
        result = []
        for item in data:
            result.append(type_name(item))
        return result

    @abstractmethod
    def set_data_to(self, obj):
        pass
