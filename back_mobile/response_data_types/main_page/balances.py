from typing import Any

import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent
from back_mobile.test_data.client import Client


class Balances(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.balances: list = self.deserialize_to_list_of(Balance, data["balances"])
        self.total_sum = data["total_sum"]

    def check(self, client: Client, **kwargs: Any):
        self.check_balances(client, **kwargs)
        self.total_sum_is_true(
            kwargs["expected_total_sum"] if "expected_total_sum" in kwargs.keys() else None
        )

    @allure.step("Проверка параметров балансов карт")
    def check_balances(self, client, **kwargs):
        for balance in self.balances:
            with allure.step(f"{balance.card_id}"):
                balance.check(client, **kwargs)

    @allure.step("Проверка общего баланса")
    def total_sum_is_true(self, expected_total_sum=None):
        if not expected_total_sum:
            expected_total_sum = 0.0
            for balance in self.balances:
                expected_total_sum += balance.balance
        self._tc.assertEqual(self.total_sum, expected_total_sum,
                             f"Общий баланс ответа ({self.total_sum}) "
                             f"не совпадает с ожидаемым ({expected_total_sum})" + self.__str__())

    def set_data_to(self, obj: Client):
        obj.cards.refresh_balances(self.balances)
        obj.cards.refresh_total_sum()


class Balance(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.balance = data["balance"]

    def check(self, client: Client, **kwargs: Any):
        self.card_id_not_empty()
        self.balance_not_null()

    @allure.step("проверка наличия card_id")
    def card_id_not_empty(self):
        self._tc.assertNotEqual(self.card_id, "",
                                f"card_id пустой" + self.__str__())

    @allure.step("проверка наличия balance")
    def balance_not_null(self):
        self._tc.assertIsNotNone(self.balance,
                                 f"balance пустой" + self.__str__())