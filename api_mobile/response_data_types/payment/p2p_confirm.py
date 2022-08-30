import allure

from api_mobile.response_data_types.response_data_base import BaseTypeParent


class P2PConfirm(BaseTypeParent):

    def set_data_to(self, obj):
        self._set_confirm_data(obj)

    @allure.step("Установить p2p_confirm клиенту")
    def _set_confirm_data(self, client):
        client.p2p_confirm = self

    def __init__(self, data: dict):
        super().__init__()
        self.commission_sum = data["commission_sum"]
        self.confirm_method = data["confirm_method"]
        self.is_confirm = data["is_confirm"]
        self.transact_id = data["transact_id"]

    def check(self, client, **kwargs):
        self.commission_sum_not_null()
        self.confirm_method_not_empty()
        self.is_confirm_not_null()
        self.transact_id_not_empty()

    @allure.step("commission_sum не пустой")
    def commission_sum_not_null(self):
        self._tc.assertIsNotNone(self.commission_sum,
                                 f"commission_sum ({self.commission_sum}) пустой" + self.__str__())

    @allure.step("confirm_method не пустой")
    def confirm_method_not_empty(self):
        self._tc.assertNotEqual(self.confirm_method, "",
                                f"confirm_method ({self.confirm_method}) пустой" + self.__str__())

    @allure.step("is_confirm не пустой")
    def is_confirm_not_null(self):
        self._tc.assertIsNotNone(self.is_confirm,
                                 f"is_confirm ({self.is_confirm}) пустой" + self.__str__())

    @allure.step("transact_id не пустой")
    def transact_id_not_empty(self):
        self._tc.assertNotEqual(self.transact_id, "",
                                f"transact_id ({self.transact_id}) пустой" + self.__str__())
