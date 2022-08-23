from abc import ABC, abstractmethod

import allure

from utils.methods import obj_to_string
from unittest import TestCase


class BaseType(ABC):

    def __init__(self):
        self.tc = TestCase()

    def __str__(self):
        return obj_to_string(self)

    @abstractmethod
    @allure.step("Проверка параметров в данных ответа")
    def check(self, client, **kwargs):
        pass
