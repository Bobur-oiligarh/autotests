import allure

from api_mobile.response_data_types.registration.sign_id import SignId
from api_mobile.test_data.client import Client


class ConfirmMethod(SignId):
    def __init__(self, data: dict):
        super().__init__(data)
        self.confirm_method = data["confirm_method"]

    def check(self, client, **kwargs):
        self.check_confirm_method(client)

    @allure.step("проверка confirm_method")
    def check_confirm_method(self, client: Client):
        self.confirm_method_not_empty()
        self.confirm_method_is_true(client.confirm_method)

    @allure.step("confirm_method не пустой")
    def confirm_method_not_empty(self):
        self.tc.assertNotEqual(self.confirm_method, "", f"confirm_method пустой" + self.__str__())

    @allure.step("confirm_method совпадает с ожидаемым")
    def confirm_method_is_true(self, expired_confirm_method):
        self.tc.assertEqual(self.confirm_method, expired_confirm_method,
                            f"confirm_method ответа ({self.confirm_method}) не "
                            f"совпадает с ожидаемым ({expired_confirm_method})" + self.__str__())

    def set_data_to(self, obj: Client):
        self.set_sign_id_and_confirm_method(obj)

    @allure.step("Установить sign_id и confirm_method")
    def set_sign_id_and_confirm_method(self, client):
        self.set_sign_id(client)
        self.set_confirm_method(client)

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.sign_id
        return self

    @allure.step("Установить confirm_method")
    def set_confirm_method(self, client):
        client.confirm_method = self.confirm_method
