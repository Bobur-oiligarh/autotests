import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType
from back_mobile.test_data.client import Client

__all__ = [
    "Operations",
    "State",
    "Operation"
]


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
        self.check_list_of("operations", client, **kwargs)
        self.check_list_of("state", client, **kwargs)


class State(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.ps_code = data["ps_code"]
        self.health = data["health"]

    def check(self, client, **kwargs):
        self.assert_not_empty("ps_code")
        self.assert_not_none("health")


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
        self.assert_not_empty("ps_code")
        self.assert_not_empty("pan")
        self.assert_not_empty("time")
        self.assert_not_none("sum")
        self.assert_not_empty("torg_name")
        self.assert_not_empty("torg_address")
        self.assert_not_empty("tran_type")
        self.assert_not_empty("curr_code")
        self.assert_not_empty("is_credit")
