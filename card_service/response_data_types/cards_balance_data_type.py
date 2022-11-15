from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.response_data_base import BaseTypeParent, BaseType
import allure


class CardsBalance(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.cards_balance: list[CardBalance] = self.deserialize_to_list_of(CardBalance, data)

    def check(self, context, **kwargs):
        self.check_list_of("cards_balance", context, **kwargs)

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    @allure.step("Установим баланс всех карт контексту")
    def set_data_to_context(self, context: CardServiceContext):
        context.cards_balance = self


class CardBalance(BaseType):
    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.balance = data["balance"]
        self.hold_mount = data["hold_mount"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_int("balance")
        self.assert_not_empty_int("hold")