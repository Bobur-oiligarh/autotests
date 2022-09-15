import allure

from utils.api_utils.response_data_base import BaseTypeParent
from api_mobile.test_data.client import Client


class SignId(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.sign_id = data["sign_id"]

    def check(self, client, **kwargs):
        self.sign_id_not_empty()

    def set_data_to(self, obj: Client):
        self.set_sign_id(obj)

    @allure.step("sign_id не пустой")
    def sign_id_not_empty(self):
        self._tc.assertNotEqual(self.sign_id, "", f"sign_id ответа пустой" + self.__str__())

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.sign_id
        return self
