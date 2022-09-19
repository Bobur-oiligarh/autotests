import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


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
        self.name_not_empty()
        self.amount_not_null()
        self.currency_not_empty()
        self.rate_not_null()
        self.months_not_null()
        self.close_data_not_empty()

    @allure.step("Name не пустой")
    def name_not_empty(self):
        self._tc.assertNotEqual(self.name, "",
                                f"Name ({self.name}) пустой" + self.__str__())

    @allure.step("Amount не пустой")
    def amount_not_null(self):
        self._tc.assertIsNotNone(self.amount,
                                 f"Amount ({self.amount}) пустой" + self.__str__())

    @allure.step("Currency не пустой")
    def currency_not_empty(self):
        self._tc.assertNotEqual(self.currency, "",
                                f"Currency ({self.currency}) пустой" + self.__str__())

    @allure.step("Rate не пустой")
    def rate_not_null(self):
        self._tc.assertIsNotNone(self.rate,
                                 f"Rate ({self.rate}) пустой" + self.__str__())

    @allure.step("Months не пустой")
    def months_not_null(self):
        self._tc.assertIsNotNone(self.months,
                                 f"Months ({self.months}) пустой" + self.__str__())

    @allure.step("CloseData не пустой")
    def close_data_not_empty(self):
        self._tc.assertNotEqual(self.close_data, "",
                                f"CloseData ({self.close_data}) пустой" + self.__str__())
