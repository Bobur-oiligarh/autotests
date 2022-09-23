import allure

from utils.api_utils.response_data_base import BaseTypeParent
from back_mobile.test_data.client import Client

__all__ = [
    "SignId"
]


class SignId(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.sign_id = data["sign_id"]

    def check(self, client, **kwargs):
        self.assert_not_empty("sign_id")

    def set_data_to(self, obj: Client):
        self.set_sign_id(obj)

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.sign_id
        return self
