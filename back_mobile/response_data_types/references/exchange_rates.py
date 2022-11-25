import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class ExchangeRates(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.exchange_rates: list[ExchangeRate] = self.deserialize_to_list_of(ExchangeRate, data)

    def set_data_to(self, context):
        self._set_exchange_rates(context)

    @allure.step("Установить курсы валют")
    def _set_exchange_rates(self, context):
        context.exchange_rates = self

    def check(self, context, **kwargs):
        self.check_list_of("exchange_rates", context, **kwargs)


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

    def check(self, context, **kwargs):
        self.assert_not_empty_str("id")
        self.assert_not_empty_str("destination")
        self.assert_not_empty_str("currency_code")
        self.assert_not_empty_str("currency_char")
        self.assert_not_empty_str("quote_currency")
        self.assert_not_empty_str("selling_rate")
        self.assert_not_empty_str("buying_rate")
        self.assert_not_empty_str("sb_course")
        self.assert_not_empty_str("begin_date")
        self.assert_not_empty_str("end_date")
        self.assert_not_empty_str("begin_sum")
        self.assert_not_empty_str("end_sum")
