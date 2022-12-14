from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class CardBinNumber(BaseTypeParent):

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
        self.assert_not_empty_str("number")
        self.assert_not_empty_str("name")
        self.assert_not_empty_str("currency_code")
        self.assert_not_empty_str("currency_id")
        self.assert_not_empty_bool("is_bank_card")
        self.assert_not_empty_bool("is_add_allowed")
        self.processing.check(context, **kwargs)
        self.assert_not_empty_str("bank_code")
        self.assert_not_none_and_true_type("bank_logo_file_id", str)
        self.assert_not_empty_str("mfo")


class Processing(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.code = data["code"]
        self.name = data["name"]
        self.is_pay_allowed = data["is_pay_allowed"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("code")
        self.assert_not_empty_str("name")
        self.assert_not_empty_bool("is_pay_allowed")
