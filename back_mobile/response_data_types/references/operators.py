import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class Operators(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.operators_list = self.deserialize_to_list_of(Operator, data)

    def set_data_to(self, obj):
        self.set_operators(obj)

    @allure.step("Установить операторы клиенту")
    def set_operators(self, context):
        context.operators = self

    def check(self, context, **kwargs):
        self.check_list_of("operators_list", context, **kwargs)


class Operator(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.operator_id = data["operator_id"]
        self.mask = data["mask"]
        self.name = data["name"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("operator_id")
        self.assert_not_empty_str("mask")
        self.assert_not_empty_str("name")
