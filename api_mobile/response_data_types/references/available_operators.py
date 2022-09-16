import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class AvailableOperators(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.operators_list = self.deserialize_to_list_of(Operator, data)

    def set_data_to(self, obj):
        self.set_operators(obj)

    @allure.step("Установить операторы клиенту")
    def set_operators(self, client):
        client.operators = self

    def check(self, client, **kwargs):
        self.check_operators(client, **kwargs)

    @allure.step("Проверка всех доступных операторов")
    def check_operators(self, client, **kwargs):
        for o in self.operators_list:
            with allure.step(f"проверка параметров {o.name}"):
                o.check(client, **kwargs)


class Operator(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.operator_id = data["operator_id"]
        self.mask = data["mask"]
        self.name = data["name"]

    def check(self, client, **kwargs):
        self.operator_id_not_empty()
        self.mask_not_empty()
        self.name_not_empty()

    @allure.step("operator_id не пустой")
    def operator_id_not_empty(self):
        self._tc.assertNotEqual(self.operator_id, "",
                                f"operator_id ({self.operator_id}) пустой" + self.__str__())

    @allure.step("mask не пустой")
    def mask_not_empty(self):
        self._tc.assertNotEqual(self.mask, "",
                                f"mask ({self.mask}) пустой" + self.__str__())

    @allure.step("name не пустой")
    def name_not_empty(self):
        self._tc.assertNotEqual(self.name, "",
                                f"name ({self.name}) пустой" + self.__str__())
