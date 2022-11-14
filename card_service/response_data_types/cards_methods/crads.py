from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "Cards",
    "Card"
]


class Card(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data.get("card_id")
        self.card_number = data.get("card_number")
        self.owner = data.get("owner")
        self.balance = data.get("balance")
        self.hold_amount = data.get("hold_amount")
        self.state = data.get("state")
        self.card_type = data.get("card_type")
        self.processing = data.get("processing")
        self.account = data.get("account")
        self.expire = data.get("expire")
        self.bank_code = data.get("bank_code")

    def check(self, context, **kwargs):
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
        self.assert_not_empty_str("bank_code")


class Cards(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.cards = self.deserialize_to_list_of(Card, data)

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    def set_data_to_context(self, obj):
        obj.cards = self

    def check(self, context, **kwargs):
        self.check_list_of("cards", context, **kwargs)
