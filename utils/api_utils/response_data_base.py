from abc import ABC, abstractmethod
from utils.methods import obj_to_string


class BaseType(ABC):
    def __str__(self):
        return obj_to_string(self)

    @abstractmethod
    def check(self, client, **kwargs):
        pass
