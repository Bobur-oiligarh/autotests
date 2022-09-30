import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent
from back_mobile.test_data.client import Client

__all__ = [
    "Cards",
    "Card"
]


class Cards(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.cards: list = self.deserialize_to_list_of(Card, data["cards"])
        self.total_sum = data["total_sum"]

    def check(self, client: Client, **kwargs):
        total_sum_uzs = 0.0
        for card in self.cards:
            with allure.step(f"проверка параметров карты {card.mask_num}"):
                card.check(client, **kwargs)
            total_sum_uzs += card.balance
        self.assert_not_empty_float("total_sum")
        self.total_sum_is_true(total_sum_uzs)

    def total_sum_is_true(self, expected_total_sum):
        self.assert_equal("total_sum", expected_total_sum)

    def get_cards_by(self, param: str = None, value=None):
        if param is None:
            return self.cards
        cards = []
        for card in self.cards:
            if value is card.__dict__[param]:
                cards.append(value)
        return cards

    @staticmethod
    def get_card_id_ps_code_from(cards, full=True):
        result = []
        for card in cards:
            result.append({"card_id" if full else "id": card.card_id, "ps_code": card.ps_code})
        return result

    def set_data_to(self, obj: Client):
        self._set_cards(obj)
        self._set_main_card(obj)

    @allure.step("Установить карты")
    def _set_cards(self, client: Client):
        client.cards = self

    @allure.step("Установить основной карту с наибольшим балансом")
    def _set_main_card(self, client: Client):
        result_card = None
        for card in self.get_cards_by():
            if result_card is None:
                result_card = card
            if card.balance > result_card.balance:
                result_card = card
        client.main_card = result_card

    @allure.step("Обновить балансы карт")
    def refresh_balances(self, balances: list):
        for balance in balances:
            for card in self.cards:
                if card.card_id == balance.card_id:
                    card.balance = balance.balance
                    break

    @allure.step("Обновить общюю сумму")
    def refresh_total_sum(self):
        total_sum = 0.0
        for card in self.cards:
            total_sum += card.balance
        self.total_sum = total_sum


class Card(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.card_type = data["card_type"]
        self.mfo = data["mfo"]
        self.mask_num = data["mask_num"]
        self.state = data["state"]
        self.balance = data["balance"]
        self.ps_code = data["ps_code"]
        self.expire = data["expire"]
        self.owner = data["owner"]

    def check(self, client, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_str("card_type")
        self.assert_not_empty_str("mfo")
        self.assert_not_empty_str("mask_num")
        self.assert_not_empty_str("state")
        self.assert_not_empty_float("balance")
        self.assert_not_empty_str("ps_code")
        self.assert_not_empty_str("expire")
        self.assert_not_empty_str("owner")
