import allure

from utils.api_utils.response_data_base import BaseType


class SignId(BaseType):

    def __init__(self, data: dict):
        self.sign_id = data["sign_id"]

    def check(self, client, **kwargs):
        self.sign_id_not_empty()

    @allure.step("sign_id не пустой")
    def sign_id_not_empty(self):
        assert self.sign_id != "", f"sign_id ответа пустой"

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.sign_id
        return self