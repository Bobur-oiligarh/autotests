import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "OpenedDeposits",
    "Deposit"
]


class OpenedDeposits(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.deposits = self.deserialize_to_list_of(Deposit, data)

    def set_data_to(self, obj):
        self.set_deposits(obj)

    @allure.step("Установить депозиты клиенту")
    def set_deposits(self, context):
        context.deposits = self

    def check(self, context, **kwargs):
        self.check_list_of("deposits", context, **kwargs)


class Deposit(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.name = data["Name"]
        self.amount = data["Amount"]
        self.currency = data["Currency"]
        self.rate = data["Rate"]
        self.months = data["Months"]
        self.close_data = data["CloseData"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("name")
        self.assert_not_empty_float("amount")
        self.assert_not_empty_str("currency")
        self.assert_not_empty_int("rate")
        self.assert_not_empty_int("months")
        self.assert_not_empty_str("close_data")
