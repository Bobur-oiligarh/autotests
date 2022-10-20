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

    def assert_no_strict_str(self, param_name):
        value = getattr(self, param_name)
        if value:
            self.assert_type_is_true(param_name, str)

    def assert_no_strict_int(self, param_name):
        value = getattr(self, param_name)
        if value:
            self.assert_type_is_true(param_name, int)

    def assert_no_strict_flo(self, param_name):
        value = getattr(self, param_name)
        if value:
            self.assert_type_is_true(param_name, float)

    def assert_no_strict_bool(self, param_name):
        value = getattr(self, param_name)
        if value:
            self.assert_type_is_true(param_name, bool)

    def assert_not_empty_str(self, param_name: str):
        self.assert_not_none_and_true_type(param_name, str)
        with allure.step(param_name + " не пустой"):
            value = getattr(self, param_name)
            self._tc.assertNotEqual(value, "", self._empty_str(param_name, value))
        return self

    def assert_not_empty_int(self, param_name: str):
        self.assert_not_none_and_true_type(param_name, int)
        return self

    def assert_not_empty_float(self, param_name: str):
        self.assert_not_none_and_true_type(param_name, float)
        return self

    def assert_not_empty_bool(self, param_name: str):
        self.assert_not_none_and_true_type(param_name, bool)
        return self

    def assert_not_none_and_true_type(self, param_name: str, expected_type: type):
        self.assert_not_none(param_name)
        self.assert_type_is_true(param_name, expected_type)
        return self

    def assert_type_is_true(self, param_name: str, expected_type: type):
        with allure.step("Проверка типа параметра " + param_name):
            value = getattr(self, param_name)
            self._tc.assertIsInstance(value, expected_type,
                                      f"Тип {param_name} ({type(value)}) не совпадает с "
                                      f"ожидаемым {expected_type.__name__}" + self.__str__())
        return self

    def assert_not_empty(self, param_name):
        self.assert_not_none(param_name)
        with allure.step(param_name + " не пустой"):
            value = getattr(self, param_name)
            self._tc.assertNotEqual(value, "", self._empty_str(param_name, value))
        return self

    def assert_not_none(self, param_name):
        value = getattr(self, param_name)
        with allure.step(param_name + " не none"):
            self._tc.assertIsNotNone(value, self._empty_str(param_name, value))
        return self

    def assert_equal(self, param_name, expected_value):
        value = getattr(self, param_name)
        with allure.step(param_name + " совпадает с ожидаемым"):
            self._tc.assertEqual(value, expected_value,
                                 f"{param_name} ({value}) не соответствует "
                                 f"ожидаемому ({expected_value})")
        return self

    def check_list_of(self, list_param_name: str, context, **kwargs):
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
