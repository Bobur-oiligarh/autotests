import allure

from utils.api_utils.response_data_base import BaseTypeParent

__all__ = [
    "ClientNameType"
]


class ClientNameType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.middle_name = data["middle_name"]

    def set_data_to(self, obj):
        self.set_name(obj)

    @allure.step("Установить имя")
    def set_name(self, context):
        context.first_name = self.first_name
        context.last_name = self.last_name
        context.middle_name = self.middle_name

    def check(self, context, **kwargs):
        self.assert_not_empty_str("first_name")
        self.assert_not_empty_str("last_name")
        self.assert_not_empty_str("middle_name")
