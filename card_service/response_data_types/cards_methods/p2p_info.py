from utils.api_utils.response_data_base import BaseTypeParent
import allure


class P2PInfo(BaseTypeParent):
    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data.get("card_id")
        self.owner = data.get("owner")
        self.pan = data.get("pan")
        self.card_type = data.get("card_type")
        self.bank_code = data.get("bank_code")
        self.processing = data.get("processing")
        self.is_bank_card = data.get("is_bank_card")
        self.expire = data.get("expire")

    def check(self, context, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_str("owner")
        self.assert_not_empty_str("pan")
        self.assert_not_empty_str("card_type")
        self.assert_not_empty_str("bank_code")
        self.assert_not_empty_str("processing")
        self.assert_not_empty_str("is_bank_card")
        self.assert_not_empty_str("expire")

    def set_data_to(self, obj):
        self.set_data_to_obj(obj)

    @allure.step("Устанавливаем информацию о P2P контексту")
    def set_data_to_obj(self, obj):
        obj.p2p_info = self
