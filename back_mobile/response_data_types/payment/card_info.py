import allure

from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseTypeParent
from . import TransactionParticipant

__all__ = [
    "CardInfo"
]


class CardInfo(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.owner = data["owner"]
        self.pan = data["pan"]
        self.expire = data["expire"]
        self.card_type = data["card_type"]
        self.bank_code = data["bank_code"]
        self.processing = data["processing"]
        self.is_bank_card = data["is_bank_card"]

    def set_data_to(self, obj: Client):
        self._set_card_info_to_client(obj)

    @allure.step("Установить параметры получателя клиенту")
    def _set_card_info_to_client(self, client: Client):
        client.receiver = TransactionParticipant({
            "id": self.card_id,
            "pan": self.pan,
            "expire": self.expire,
            "ps_code": self.processing,
            "bank_code": self.bank_code,
            "owner": self.owner
        })

    def check(self, client: Client, **kwargs):
        self.assert_not_empty_str("card_id")
        self.assert_not_empty_str("owner")
        self.assert_not_empty_str("pan")
        self.assert_not_empty_str("expire")
        self.assert_not_empty_str("card_type")
        self.assert_not_empty_str("bank_code")
        self.assert_not_empty_str("processing")
        self.assert_not_empty_bool("is_bank_card")
