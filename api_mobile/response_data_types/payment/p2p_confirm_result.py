import allure

from api_mobile.response_data_types.response_data_base import BaseTypeParent


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
        self.product_name_not_empty()
        self.transact_id_not_empty()
        self.sender_name_not_empty()
        self.sender_pan_not_empty()
        self.receiver_name_not_empty()
        self.receiver_pan_not_empty()
        self.sum_not_null()
        self.commission_sum_not_null()
        self.status_not_empty()
        self.operation_time_not_empty()

    @allure.step("product_name не пустой")
    def product_name_not_empty(self):
        self._tc.assertNotEqual(self.product_name, "",
                                f"product_name ({self.product_name}) пустой" + self.__str__())

    @allure.step("transact_id не пустой")
    def transact_id_not_empty(self):
        self._tc.assertNotEqual(self.transact_id, "",
                                f"transact_id ({self.transact_id}) пустой" + self.__str__())

    @allure.step("sender_name не пустой")
    def sender_name_not_empty(self):
        self._tc.assertNotEqual(self.sender_name, "",
                                f"sender_name ({self.sender_name}) пустой" + self.__str__())

    @allure.step("sender_pan не пустой")
    def sender_pan_not_empty(self):
        self._tc.assertNotEqual(self.sender_pan, "",
                                f"sender_pan ({self.sender_pan}) пустой" + self.__str__())

    @allure.step("receiver_name не пустой")
    def receiver_name_not_empty(self):
        self._tc.assertNotEqual(self.receiver_name, "",
                                f"receiver_name ({self.receiver_name}) пустой" + self.__str__())

    @allure.step("receiver_pan не пустой")
    def receiver_pan_not_empty(self):
        self._tc.assertNotEqual(self.receiver_pan, "",
                                f"receiver_pan ({self.receiver_pan}) пустой" + self.__str__())

    @allure.step("sum не пустой")
    def sum_not_null(self):
        self._tc.assertIsNotNone(self.sum,
                                 f"sum ({self.sum}) пустой" + self.__str__())

    @allure.step("commission_sum не пустой")
    def commission_sum_not_null(self):
        self._tc.assertIsNotNone(self.commission_sum,
                                 f"commission_sum ({self.commission_sum} пустой" + self.__str__())

    @allure.step("status не пустой")
    def status_not_empty(self):
        self._tc.assertNotEqual(self.status, "",
                                f"status ({self.status}) пустой" + self.__str__())

    @allure.step("operation_time не пустой")
    def operation_time_not_empty(self):
        self._tc.assertNotEqual(self.operation_time, "",
                                f"operation_time ({self.operation_time}) пустой" + self.__str__())
