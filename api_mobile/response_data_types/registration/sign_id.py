import allure

from api_mobile.response_data_types.response_data_base import BaseType


class SignId(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.sign_id = data["sign_id"]

    def check(self, client, **kwargs):
        self.sign_id_not_empty()

    @allure.step("sign_id не пустой")
    def sign_id_not_empty(self):
        self.tc.assertNotEqual(self.sign_id, "", f"sign_id ответа пустой" + self.__str__())

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.sign_id
        return self
