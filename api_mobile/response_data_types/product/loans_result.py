import allure

from api_mobile.response_data_types.response_data_base import BaseTypeParent, BaseType


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
        self.name_not_empty()
        self.amount_not_null()
        self.currency_not_empty()
        self.rate_not_null()
        self.graph_day_not_empty()
        self.graph_amount_not_null()
        self.close_data_not_null()

    @allure.step("name не пустой")
    def name_not_empty(self):
        self._tc.assertNotEqual(self.name, "",
                                f"name ({self.name}) пустой" + self.__str__())

    @allure.step("amount не пустой")
    def amount_not_null(self):
        self._tc.assertIsNotNone(self.amount,
                                 f"amount ({self.amount}) пустой" + self.__str__())

    @allure.step("currency не пустой")
    def currency_not_empty(self):
        self._tc.assertNotEqual(self.currency, "",
                                f"currency ({self.currency}) пустой" + self.__str__())

    @allure.step("rate не пустой")
    def rate_not_null(self):
        self._tc.assertIsNotNone(self.rate,
                                 f"rate ({self.rate}) пустой" + self.__str__())

    @allure.step("graph_day не пустой")
    def graph_day_not_empty(self):
        self._tc.assertNotEqual(self.graph_day, "",
                                f"graph_day ({self.graph_day}) пустой" + self.__str__())

    @allure.step("graph_amount не пустой")
    def graph_amount_not_null(self):
        self._tc.assertIsNotNone(self.graph_amount,
                                 f"graph_amount ({self.graph_amount}) пустой" + self.__str__())

    @allure.step("close_data не пустой")
    def close_data_not_null(self):
        self._tc.assertNotEqual(self.close_data, "",
                                f"close_data ({self.close_data}) пустой" + self.__str__())
