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
    def set_deposits(self, client):
        client.deposits = self

    def check(self, client, **kwargs):
        self.check_all_deposits(client, **kwargs)

    @allure.step("Проверка всех депозитов")
    def check_all_deposits(self, client, **kwargs):
        for deposit in self.deposits:
            with allure.step(f"Проверка параметров {deposit.name}"):
                deposit.check(client, **kwargs)


class Deposit(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.name = data["Name"]
        self.amount = data["Amount"]
        self.currency = data["Currency"]
        self.rate = data["Rate"]
        self.months = data["Months"]
        self.close_data = data["CloseData"]

    def check(self, client, **kwargs):
        self.assert_not_empty("name")
        self.assert_not_empty("amount")
        self.assert_not_empty("currency")
        self.assert_not_empty("rate")
        self.assert_not_empty("months")
        self.assert_not_empty("close_data")
