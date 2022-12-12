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

    def assert_no_strict_str(self, param_name: str):
        value = getattr(self, param_name)
        if value:
            self.assert_not_empty_str(param_name)

    def assert_no_strict_int(self, param_name: str):
        value = getattr(self, param_name)
        if value:
            self.assert_not_empty_int(param_name)

    def assert_no_strict_float(self, param_name: str):
        value = getattr(self, param_name)
        if value:
            self.assert_not_empty_float(param_name)

    def assert_no_strict_bool(self, param_name: str):
        value = getattr(self, param_name)
        if value:
            self.assert_not_empty_bool(param_name)

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

    def assert_not_empty_balance(self, param_name: str):
        self.assert_not_none(param_name)
        with allure.step("проверка типа баланса"):
            self.assert_not_empty_numeric(param_name)

    def assert_not_empty_numeric(self, param_name: str):
        self.assert_not_none(param_name)
        with allure.step("проверка числового типа параметра"):
            if type(getattr(self, param_name)) in [float, int]:
                return self
            assert False, f"тип данных баланса не соответствует числовому {type(getattr(self, param_name))}\n{self.__str__()}"

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

    def assert_equal_param(self, param_name, expected_value):
        value = getattr(self, param_name)
        with allure.step(param_name + " совпадает с ожидаемым"):
            self._tc.assertEqual(value, expected_value,
                                 f"{param_name} ({value}) не соответствует "
                                 f"ожидаемому ({expected_value})")
        return self

    def assert_equal(self, obj):
        differences = self._differences(obj)
        self._tc.assertEqual(0, len(differences),
                             f"Результаты сопоставления объектов {differences} не соответствуют ожидаемым")

    def assert_not_equal(self, obj):
        differences = self._differences(obj)
        self._tc.assertNotEqual(0, len(differences),
                                f"Результаты сопоставления объектов {differences} не соответствуют ожидаемым")

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

    def _differences(self, obj) -> list:
        differences = []
        for key in self.__dict__.keys():
            if self.__dict__[key] != obj.__dict__[key]:
                differences.append([key, self.__dict__[key], obj.__dict__[key]])
        return differences


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

    def get_obj_by_param(self, list_param_name, param_name, param_value):
        result = None
        for item in getattr(self, list_param_name):
            if item.__dict__[param_name] == param_value:
                result = item
                break
        return result

    def assert_obj_exist(self, list_param_name, param_name, param_value):
        self._tc.assertTrue(
            True if self.get_obj_by_param(list_param_name, param_name, param_value) else False,
            f"Объекта {param_name} - {param_value} нет в списке {getattr(self, list_param_name)}"
        )

    def assert_obj_not_exist(self, list_param_name, param_name, param_value):
        self._tc.assertFalse(
            False if not self.get_obj_by_param(list_param_name, param_name, param_value) else True,
            f"Такой объект присутствует в списке"
        )
