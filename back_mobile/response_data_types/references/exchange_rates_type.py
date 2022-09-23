import allure

from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "ExchangeRateList",
    "ExchangeRate"
]


class ExchangeRateList(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.exchange_rates: list[ExchangeRate] = self.deserialize_to_list_of(ExchangeRate, data)

    def set_data_to(self, client: Client):
        self._set_exchange_rates(client)

    @allure.step("Установить курсы валют")
    def _set_exchange_rates(self, client: Client):
        client.exchange_rates = self

    def check(self, client: Client, **kwargs):
        self.check_exchange_rates(client, **kwargs)

    @allure.step("Проверка параметров курсов валют")
    def check_exchange_rates(self, client: Client, **kwargs):
        for exchange_rate in self.exchange_rates:
            with allure.step(f"currency {exchange_rate.currency_char}"):
                exchange_rate.check(client, **kwargs)


class ExchangeRate(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.id = data['Id']
        self.destination = data['Destination']
        self.currency_code = data['CurrencyCode']
        self.currency_char = data['CurrencyChar']
        self.quote_currency = data['QuoteCurrency']
        self.selling_rate = data['SellingRate']
        self.buying_rate = data['BuyingRate']
        self.sb_course = data['SbCourse']
        self.begin_date = data['BeginDate']
        self.end_date = data['EndDate']
        self.begin_sum = data['BeginSum']
        self.end_sum = data['EndSum']

    def check(self, client: Client, **kwargs):
        self.assert_not_empty("id")
        self.assert_not_empty("destination")
        self.assert_not_empty("currency_code")
        self.assert_not_empty("currency_char")
        self.assert_not_empty("quote_currency")
        self.assert_not_empty("selling_rate")
        self.assert_not_empty("buying_rate")
        self.assert_not_empty("sb_course")
        self.assert_not_empty("begin_date")
        self.assert_not_empty("end_date")
        self.assert_not_empty("begin_sum")
        self.assert_not_empty("end_sum")
