import allure

from utils.api_utils.response_data_base import BaseTypeParent

__all__ = [
    "P2PConfirmResult"
]


class P2PConfirmResult(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.product_name = data["product_name"]
        self.transact_id = data["transact_id"]
        self.sender_name = data["sender_name"]
        self.sender_pan = data["sender_pan"]
        self.receiver_name = data["receiver_name"]
        self.receiver_pan = data["receiver_pan"]
        self.sum = data["sum"]
        self.commission_sum = data["commission_sum"]
        self.status = data["status"]
        self.operation_time = data["operation_time"]

    def set_data_to(self, obj):
        self._set_operation_check(obj)

    @allure.step("Установить чек операции клиенту")
    def _set_operation_check(self, client):
        client.operation_check = self

    def check(self, client, **kwargs):
        self.assert_not_empty_str("product_name")
        self.assert_not_empty_str("transact_id")
        self.assert_not_empty_str("sender_name")
        self.assert_not_empty_str("sender_pan")
        self.assert_not_empty_str("receiver_name")
        self.assert_not_empty_str("receiver_pan")
        self.assert_not_empty_int("sum")
        self.assert_not_empty_int("commission_sum")
        self.assert_not_empty_str("status")
        self.assert_not_empty_str("operation_time")
