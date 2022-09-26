from abc import ABC, abstractmethod

import allure

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
    def check(self, context, **kwargs):
        pass

    def assert_not_empty(self, param_name):
        self.assert_not_none(param_name)
        value = getattr(self, param_name)
        with allure.step(param_name + " не пустой"):
            self._tc.assertNotEqual(value, "", self._empty_str(param_name, value))
        return self

    def assert_not_none(self, param_name):
        value = getattr(self, param_name)
        with allure.step(param_name + " не пустой"):
            self._tc.assertIsNotNone(value, self._empty_str(param_name, value))
        return self

    def assert_equal(self, param_name, expected_value):
        value = getattr(self, param_name)
        with allure.step(param_name + " совпадает с ожидаемым"):
            self._tc.assertEqual(value, expected_value,
                                 f"{param_name} ({value}) не соответствует "
                                 f"ожидаемому ({expected_value})")
        return self

    def check_list_of(self, list_param_name, context, **kwargs):
        with allure.step(f"Проверка объектов в списке {list_param_name}"):
            i = 0
            for item in getattr(self, list_param_name):
                with allure.step(f"Проверка параметров {type(item)} - {i}"):
                    item.check(context, **kwargs)
                i += 1

    def check_attrs_of(self, param_name, context, **kwargs):
        with allure.step("Проверка параметров " + param_name):
            getattr(self, param_name).check(context, **kwargs)
        return self

    def _empty_str(self, parameter_name, value):
        return parameter_name + f" ({value}) пустой" + self.__str__()


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
