import unittest

import allure
from utils.api_utils.response_data_base import BaseTypeParent


class SMEStrategies(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.strategies: list[SMEStrategy] = self.deserialize_to_list_of(SMEStrategy, data)

    def check(self, context, **kwargs):
        self.check_list_of("strategies", context)

    def set_data_to(self, obj):
        self.set_data_to_obj(obj)

    @allure.step("Установим стратегии контексту")
    def set_data_to_obj(self, obj):
        obj.strategies = self

    def get_strategy_by_param(self, param_name: str, param_value):
        strategy = None
        for strategy_obj in self.strategies:
            if strategy_obj.__dict__[param_name] == param_value:
                return strategy
        return strategy

    def exist(self, param_name: str, param_value):
        self._tc.assertTrue(self.get_strategy_by_param(param_name, param_value))

    def not_exist(self, param_name: str, param_value):
        self._tc.assertFalse(self.get_strategy_by_param(param_name, param_value))


class SMEStrategy(BaseTypeParent):
    def __init__(self, data: dict):
        super().__init__()
        self.id = data.get("id")
        self.product_id = data.get("product_id")
        self.step_id = data.get("step_id")
        self.user_employee = data.get("user_employee")
        self.active = data.get("active")
        self.created_at = data.get("created_at")

    def check(self, context, **kwargs):
        self.assert_not_empty_str("id")
        self.assert_not_empty_str("product_id")
        self.assert_not_empty_str("step_id")
        self.assert_not_empty_str("user_employee")
        self.assert_not_empty_bool("active")
        self.assert_not_empty_str("created_at")

    def set_data_to(self, obj):
        self.set_strategy_to(obj)

    @allure.step("Сохраняем аккаунт контексту")
    def set_strategy_to(self, obj):
        obj.strategy = self

    def change_param_value(self, param_name: str, param_value):
        self.__setattr__(param_name, param_value)

    def check_objects_similarity(self, strategy: object):
        for attribute in self.__dict__.keys():
            if attribute in




if __name__ == '__main__':
    class Test:
        def __init__(self):
            self.book = "jhbj"
            self.note = "sfgf"

    a = Test()
    print(a.__dict__.keys()["book"])
    unittest.TestCase().assertTrue(a)