from typing import Any
import allure
from utils.api_utils.response_data_base import BaseTypeParent, BaseType
from api_mobile.test_data.client import Client


class ExchangeRateList(BaseTypeParent):
    """Generates exchange rates for all currency type."""

    def __init__(self, data: list):
        super().__init__()
        self.exchange_rates: list[ExchangeRateType] = self.deserialize_to_list_of(ExchangeRateType, data)

    def set_data_to(self, client: Client):
        self._set_exchange_rates(client)

    @allure.step("Установить курсы клиенту")
    def _set_exchange_rates(self, client: Client):
        client.exchange_rates = self

    def check(self, client: Client, **kwargs: Any):
        self.check_exchange_rates(client, **kwargs)

    @allure.step("Проверка параметров курсов.")
    def check_exchange_rates(self, client: Client, **kwargs):
        for exchange_rate in self.exchange_rates:
            with allure.step(f"currency {exchange_rate.currency_char}"):
                exchange_rate.check(client, **kwargs)


class ExchangeRateType(BaseType):
    """Implements exchange rate data type class."""

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

    def check(self, client, **kwargs):
        self.check_id()
        self.check_destination()
        self.check_currency_code()
        self.check_currency_char()
        self.check_quote_currency()
        self.check_selling_rate()
        self.check_buying_rate()
        self.check_sb_course()
        self.check_begin_date()
        self.check_end_date()
        self.check_begin_sum()
        self.check_end_sum()

    @allure.step("Id валюты")
    def check_id(self):
        self._tc.assertNotEqual(self.id, "",
                                f"id валюты ({self.id}) пустой" + self.__str__())

    @allure.step("Destination не пустой")
    def check_destination(self):
        self._tc.assertNotEqual(self.destination, "",
                                f"destination ({self.destination}) пустой" + self.__str__())

    @allure.step("Currency_code не пустой")
    def check_currency_code(self):
        self._tc.assertNotEqual(self.currency_code, "",
                                f"destination ({self.currency_code}) пустой" + self.__str__())

    @allure.step("Currency_char не пустой")
    def check_currency_char(self):
        self._tc.assertNotEqual(self.currency_char, "",
                                f"destination ({self.currency_char}) пустой" + self.__str__())

    @allure.step("Quote_currency не пустой")
    def check_quote_currency(self):
        self._tc.assertNotEqual(self.quote_currency, "",
                                f"destination ({self.quote_currency}) пустой" + self.__str__())

    @allure.step("Selling_rate не пустой")
    def check_selling_rate(self):
        self._tc.assertNotEqual(self.selling_rate, "",
                                f"destination ({self.selling_rate}) пустой" + self.__str__())

    @allure.step("Buying_rate не пустой")
    def check_buying_rate(self):
        self._tc.assertNotEqual(self.buying_rate, "",
                                f"destination ({self.buying_rate}) пустой" + self.__str__())

    @allure.step("Sb_course не пустой")
    def check_sb_course(self):
        self._tc.assertNotEqual(self.sb_course, "",
                                f"destination ({self.sb_course}) пустой" + self.__str__())

    @allure.step("Begin_date не пустой")
    def check_begin_date(self):
        self._tc.assertNotEqual(self.begin_date, "",
                                f"destination ({self.begin_date}) пустой" + self.__str__())

    @allure.step("End_date не пустой")
    def check_end_date(self):
        self._tc.assertNotEqual(self.end_date, "",
                                f"destination ({self.end_date}) пустой" + self.__str__())

    @allure.step("Begin_sum, не пустой")
    def check_begin_sum(self):
        self._tc.assertNotEqual(self.begin_sum, "",
                                f"destination ({self.begin_sum}) пустой" + self.__str__())

    @allure.step("End_sum не пустой")
    def check_end_sum(self):
        self._tc.assertNotEqual(self.end_sum, "",
                                f"destination ({self.end_sum}) пустой" + self.__str__())
