import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class Loans(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.loans_list: list[Loan] = self.deserialize_to_list_of(Loan, data)

    def set_data_to(self, obj):
        self.set_loans_to_client(obj)

    @allure.step("Установить кредиты клиенту")
    def set_loans_to_client(self, context):
        context.loans = self

    def check(self, context, **kwargs):
        self.check_list_of("loans_list", context, **kwargs)


class Loan(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.name = data["Name"]
        self.amount = data["Amount"]
        self.currency = data["Currency"]
        self.rate = data["Rate"]
        self.graph_day = data["GraphDay"]
        self.graph_amount = data["GraphAmount"]
        self.close_data = data["CloseData"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("name")
        self.assert_not_empty_float("amount")
        self.assert_not_empty_str("currency")
        self.assert_not_empty_int("rate")
        self.assert_not_empty_str("graph_day")
        self.assert_not_empty_float("graph_amount")
        self.assert_not_empty_str("close_data")
