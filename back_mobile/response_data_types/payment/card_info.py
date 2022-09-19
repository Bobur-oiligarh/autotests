from typing import Any

import allure

from back_mobile.response_data_types.payment.templates import TransactionParticipant
from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseTypeParent


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

    def check(self, client: Client, **kwargs: Any):
        self.card_id_not_empty()
        self.owner_not_empty()
        self.pan_not_empty()
        self.expire_not_empty()
        self.card_type_not_empty()
        self.bank_code_not_empty()
        self.processing_not_empty()
        self.is_bank_card_not_null()

    @allure.step("card_id не пустой")
    def card_id_not_empty(self):
        self._tc.assertNotEqual(self.card_id, "",
                                f"card_id ({self.card_id}) пустой" + self.__str__())

    @allure.step("owner не пустой")
    def owner_not_empty(self):
        self._tc.assertNotEqual(self.owner, "",
                                f"owner ({self.owner} пустой" + self.__str__())

    @allure.step("pan не пустой")
    def pan_not_empty(self):
        self._tc.assertNotEqual(self.pan, "",
                                f"pan ({self.pan}) пустой" + self.__str__())

    @allure.step("expire не пустой")
    def expire_not_empty(self):
        self._tc.assertNotEqual(self.expire, "",
                                f"expire ({self.expire}) пустой" + self.__str__())

    @allure.step("card_type не пустой")
    def card_type_not_empty(self):
        self._tc.assertNotEqual(self.card_type, "",
                                f"card_type ({self.card_type}) пустой" + self.__str__())

    @allure.step("bank_code не пустой")
    def bank_code_not_empty(self):
        self._tc.assertNotEqual(self.bank_code, "",
                                f"bank_code ({self.bank_code}) пустой" + self.__str__())

    @allure.step("processing не пустой")
    def processing_not_empty(self):
        self._tc.assertNotEqual(self.processing, "",
                                f"processing ({self.processing}) пустой" + self.__str__())

    @allure.step("is_bank_card не пустой")
    def is_bank_card_not_null(self):
        self._tc.assertIsNotNone(self.is_bank_card,
                                 f"is_bank_card ({self.is_bank_card}) пустой" + self.__str__())
