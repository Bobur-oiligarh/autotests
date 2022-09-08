import allure

from api_mobile.response_data_types.response_data_base import BaseTypeParent
from api_mobile.test_data.client import Client


class ClientNameType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.middle_name = data["middle_name"]

    def set_data_to(self, obj: Client):
        self.set_name(obj)
        pass

    @allure.step("Установить имя")
    def set_name(self, client):
        client.first_name = self.first_name
        client.last_name = self.last_name
        client.middle_name = self.middle_name

    def check(self, client, **kwargs):
        self.first_name_not_empty()
        self.last_name_not_empty()
        self.middle_name_not_empty()

    @allure.step("проверка наличия first_name")
    def first_name_not_empty(self):
        self._tc.assertNotEqual(self.first_name, "",
                                f"first_name пустой" + self.__str__())

    @allure.step("проверка наличия last_name")
    def last_name_not_empty(self):
        self._tc.assertNotEqual(self.last_name, "",
                                f"last_name пустой" + self.__str__())

    @allure.step("проверка наличия middle_name")
    def middle_name_not_empty(self):
        self._tc.assertNotEqual(self.middle_name, "",
                                f"middle_name пустой")
