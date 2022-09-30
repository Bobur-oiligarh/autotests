import allure

from utils.api_utils.response_data_base import BaseTypeParent
from back_mobile.test_data.client import Client

__all__ = [
    "ClientNameType"
]


class ClientNameType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.middle_name = data["middle_name"]

    def set_data_to(self, obj: Client):
        self.set_name(obj)

    @allure.step("Установить имя")
    def set_name(self, client):
        client.first_name = self.first_name
        client.last_name = self.last_name
        client.middle_name = self.middle_name

    def check(self, client, **kwargs):
        self.assert_not_empty_str("first_name")
        self.assert_not_empty_str("last_name")
        self.assert_not_empty_str("middle_name")
