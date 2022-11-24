import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class Operations(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.operations = self.deserialize_to_list_of(Operation, data["operations"])
        self.state = self.deserialize_to_list_of(State, data["state"])

    def set_data_to(self, obj):
        self.set_operations(obj)

    @allure.step("Установть операции")
    def set_operations(self, context):
        context.operations = self.operations

    def check(self, context, **kwargs):
        self.check_list_of("operations", context, **kwargs)
        self.check_list_of("state", context, **kwargs)


class State(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.ps_code = data["ps_code"]
        self.health = data["health"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("ps_code")
        self.assert_not_empty_bool("health")


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

    def check(self, context, **kwargs):
        self.assert_not_empty_str("ps_code")
        self.assert_not_empty_str("pan")
        self.assert_not_empty_str("time")
        self.assert_not_empty_int("sum")
        self.assert_not_empty_str("torg_name")
        self.assert_not_empty_str("torg_address")
        self.assert_not_empty_str("tran_type")
        self.assert_not_empty_str("curr_code")
        self.assert_not_empty_bool("is_credit")
