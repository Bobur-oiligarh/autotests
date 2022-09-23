import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "LoansResult",
    "Loan"
]


class LoansResult(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.loans_list: list[Loan] = self.deserialize_to_list_of(Loan, data)

    def set_data_to(self, obj):
        self.set_loans_to_client(obj)

    @allure.step("Установить кредиты клиенту")
    def set_loans_to_client(self, client):
        client.loans = self

    def check(self, client, **kwargs):
        self.check_all_loans(client, **kwargs)

    @allure.step("Проверка кредитов")
    def check_all_loans(self, client, **kwargs):
        for loan in self.loans_list:
            with allure.step(f"Проверка параметров loan - {loan.name}"):
                loan.check(client, **kwargs)


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

    def check(self, client, **kwargs):
        self.assert_not_empty("name")
        self.assert_not_empty("amount")
        self.assert_not_empty("currency")
        self.assert_not_empty("rate")
        self.assert_not_empty("graph_day")
        self.assert_not_empty("graph_amount")
        self.assert_not_empty("close_data")
