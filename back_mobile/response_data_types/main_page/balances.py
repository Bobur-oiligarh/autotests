import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class Balances(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.balances: list = self.deserialize_to_list_of(Balance, data["balances"])
        self.total_sum = data["total_sum"]

    def check(self, context, **kwargs):
        self.check_list_of("balances", context, **kwargs)
        self.total_sum_is_true(
            kwargs["expected_total_sum"] if "expected_total_sum" in kwargs.keys() else None
        )

    @allure.step("Проверка общего баланса")
    def total_sum_is_true(self, expected_total_sum=None):
        if not expected_total_sum:
            expected_total_sum = 0.0
            for balance in self.balances:
                expected_total_sum += balance.balance
        self.assert_not_empty_float("total_sum")
        self.assert_equal_param("total_sum", expected_total_sum)

    def set_data_to(self, obj):
        self.update_client_balances_and_total_sum(obj)

    @allure.step("Обновить балансы карт клиента и общую сумму")
    def update_client_balances_and_total_sum(self, context):
        context.cards.refresh_balances(self.balances)
        context.cards.refresh_total_sum()


class Balance(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.balance = data["balance"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_float("balance")
