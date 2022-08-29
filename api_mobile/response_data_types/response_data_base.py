from abc import ABC, abstractmethod

from utils.methods import obj_to_string
from unittest import TestCase


class BaseType(ABC):

    def __init__(self):
        self.tc = TestCase()

    def __str__(self):
        return obj_to_string(self)

    @abstractmethod
    def check(self, client, **kwargs):
        pass


class BaseTypeParent(BaseType, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_data_to(self, obj):
        pass