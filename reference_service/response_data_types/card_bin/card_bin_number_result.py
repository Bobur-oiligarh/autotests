from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = [
    "CardBinNumberResult",
    "Processing"
]


class CardBinNumberResult(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.number = data["number"]
        self.name = data["name"]
        self.currency_code = data["currency_code"]
        self.currency_id = data["currency_id"]
        self.is_bank_card = data["is_bank_card"]
        self.is_add_allowed = data["is_add_allowed"]
        self.processing = Processing(data["processing"])
        self.bank_code = data["bank_code"]
        self.bank_logo_file_id = data["bank_logo_file_id"]
        self.mfo = data["mfo"]

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    def set_data_to_context(self, context):
        context.card_bins = self

    def check(self, context, **kwargs):
        self.assert_not_empty("number")
        self.assert_not_empty("name")
        self.assert_not_empty("currency_code")
        self.assert_not_empty("currency_id")
        self.assert_not_none("is_bank_card")
        self.assert_not_none("is_add_allowed")
        self.processing.check(context, **kwargs)
        self.assert_not_empty("bank_code")
        self.assert_not_none("bank_logo_file_id")
        self.assert_not_empty("mfo")


class Processing(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.code = data["code"]
        self.name = data["name"]
        self.is_pay_allowed = data["is_pay_allowed"]

    def check(self, context, **kwargs):
        self.assert_not_empty("code")
        self.assert_not_empty("name")
        self.assert_not_none("is_pay_allowed")
