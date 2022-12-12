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
        result = None
        for strategy_obj in self.strategies:
            if strategy_obj.__dict__[param_name] == param_value:
                result = strategy_obj
                return result
        return result


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

    @allure.step("Изменение значения параметра объекта strategy: {param_name} на {param_value}")
    def change_param_value(self, param_name: str, param_value):
        self.__setattr__(param_name, param_value)
