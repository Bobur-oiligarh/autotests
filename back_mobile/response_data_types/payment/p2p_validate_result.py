import allure

from utils.api_utils.response_data_base import BaseTypeParent

__all__ = [
    "P2PValidateResult"
]


class P2PValidateResult(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.commission_sum = data["commission_sum"]
        self.confirm_method = data["confirm_method"]
        self.is_confirm = data["is_confirm"]
        self.transact_id = data["transact_id"]

    def set_data_to(self, obj):
        self._set_confirm_data(obj)

    @allure.step("Установить p2p_confirm клиенту")
    def _set_confirm_data(self, client):
        client.p2p_validate_result = self

    def check(self, client, **kwargs):
        self.assert_not_none("commission_sum")
        self.assert_not_empty("confirm_method")
        self.assert_not_none("is_confirm")
        self.assert_not_empty("transact_id")
