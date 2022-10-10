import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "InfoCards",
    "InfoCard"
]


class InfoCards(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.cards_list: list[InfoCard] = self.deserialize_to_list_of(InfoCard, data)

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    @allure.step("Установить карты в переменную контекста")
    def set_data_to_context(self, context):
        context.cards = self

    def check(self, context, **kwargs):
        self.check_list_of("cards_list", context, **kwargs)


class InfoCard(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.card_number = data["card_number"]
        self.owner = data["owner"]
        self.balance = data["balance"]
        self.hold_amount = data["hold_amount"]
        self.state = data["state"]
        self.card_type = data["card_type"]
        self.processing = data["processing"]
        self.account = data["account"]
        self.expire = data["expire"]
        self.bank_code = data["bank_code"]

    def check(self, client, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_str("card_number")
        self.assert_not_empty_str("owner")
        self.assert_not_empty_int("balance")
        self.assert_not_empty_int("hold_amount")
        self.assert_not_empty_str("state")
        self.assert_not_empty_str("card_type")
        self.assert_not_empty_str("processing")
        self.assert_not_empty_str("account")
        self.assert_not_empty_str("expire")
        self.assert_not_none_and_true_type("bank_code", str)
