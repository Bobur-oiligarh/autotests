import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType
from back_mobile.test_data.client import Client


class Operations(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.operations = self.deserialize_to_list_of(Operation, data["operations"])
        self.state = self.deserialize_to_list_of(State, data["state"])

    def set_data_to(self, obj: Client):
        self.set_operations(obj)

    @allure.step("Установть операции")
    def set_operations(self, client):
        client.operations = self.operations

    def check(self, client, **kwargs):
        self.check_operations(client, **kwargs)
        self.check_states(client, **kwargs)

    @allure.step("Проверика операций")
    def check_operations(self, client, **kwargs):
        for operation in self.operations:
            with allure.step(
                    f"проверка параметров операции {operation.torg_name} {operation.pan}"
            ):
                operation.check(client, **kwargs)

    @allure.step("Проверка состояний процессингов")
    def check_states(self, client, **kwargs):
        for state in self.state:
            with allure.step(f"проверка параметров состояния процессинга {state.ps_code}"):
                state.check(client, **kwargs)


class State(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.ps_code = data["ps_code"]
        self.health = data["health"]

    def check(self, client, **kwargs):
        self.ps_code_not_empty()
        self.health_not_null()

    @allure.step("ps_code не пустой")
    def ps_code_not_empty(self):
        self._tc.assertNotEqual(self.ps_code, "",
                                f"ps_code пустой" + self.__str__())

    @allure.step("health не пустой")
    def health_not_null(self):
        self._tc.assertIsInstance(self.health, bool,
                                  f"health пустой" + self.__str__())


class Operation(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.ps_code = data["ps_code"]
        self.pan = data["pan"]
        self.time = data["time"]
        self.sum = data["sum"]
        self.torg_name = data["torg_name"]
        self.torg_address = data["torg_address"]
        self.tran_type = data["tran_type"]
        self.curr_code = data["curr_code"]
        self.is_credit = data["is_credit"]

    def check(self, client, **kwargs):
        self.ps_code_not_empty()
        self.pan_not_empty()
        self.time_not_empty()
        self.sum_not_null()
        self.torg_name_not_empty()
        self.torg_address_not_empty()
        self.tran_type_not_empty()
        self.curr_code_not_empty()
        self.is_credit_not_empty()

    @allure.step("ps_code не пустой")
    def ps_code_not_empty(self):
        self._tc.assertNotEqual(self.ps_code, "",
                                f"ps_code пустой" + self.__str__())

    @allure.step("pan не пустой")
    def pan_not_empty(self):
        self._tc.assertNotEqual(self.pan, "",
                                f"pan пустой" + self.__str__())

    @allure.step("time не пустой")
    def time_not_empty(self):
        self._tc.assertNotEqual(self.time, "",
                                f"time пустой" + self.__str__())

    @allure.step("sum не null")
    def sum_not_null(self):
        self._tc.assertIsNotNone(self.sum,
                                 f"sum является null" + self.__str__())

    @allure.step("torg_name не пустой")
    def torg_name_not_empty(self):
        self._tc.assertNotEqual(self.torg_name, "",
                                f"torg_name пустой" + self.__str__())

    @allure.step("torg_address не пустой")
    def torg_address_not_empty(self):
        self._tc.assertNotEqual(self.torg_address, "",
                                f"torg_address пустой" + self.__str__())

    @allure.step("tran_type не пустой")
    def tran_type_not_empty(self):
        self._tc.assertNotEqual(self.tran_type, "",
                                f"tran_type пустой" + self.__str__())

    @allure.step("curr_code не пустой")
    def curr_code_not_empty(self):
        self._tc.assertNotEqual(self.curr_code, "",
                                f"curr_code пустой" + self.__str__())

    @allure.step("is_credit не пустой")
    def is_credit_not_empty(self):
        self._tc.assertIsInstance(self.is_credit, bool,
                                  f"is_credit пустой" + self.__str__())
