import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class Templates(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.templates: list = self.deserialize_to_list_of(Template, data)

    def set_data_to(self, obj):
        self._set_templates_to_client(obj)

    @allure.step("Установить шаблоны")
    def _set_templates_to_client(self, client):
        client.templates = self

    def check(self, client, **kwargs):
        for template in self.templates:
            with allure.step(f"Проверка шаблона {template.template_id}"):
                template.check(client, **kwargs)


class Template(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.sender = TransactionParticipant(data["sender"])
        self.receiver = TransactionParticipant(data["receiver"])
        self.sum = data["sum"]
        self.commission_sum = data["commission_sum"]
        self.status = data["status"]
        self.operation_time = data["operation_time"]
        self.template_id = data["template_id"]

    def check(self, client, **kwargs):
        self.check_sender_params(client, **kwargs)
        self.check_receiver_params(client, **kwargs)
        self.sum_not_null()
        self.commission_sum_not_null()
        self.status_not_empty()
        self.operation_time_not_empty()
        self.template_id_not_empty()

    @allure.step("Проверка параметров отправителя")
    def check_sender_params(self, client, **kwargs):
        self.sender.check(client, **kwargs)

    @allure.step("проверка параметров получателя")
    def check_receiver_params(self, client, **kwargs):
        self.receiver.check(client, **kwargs)

    @allure.step("sum не пустой")
    def sum_not_null(self):
        self._tc.assertIsNotNone(self.sum,
                                 f"sum ({self.sum}) пустой" + self.__str__())

    @allure.step("commission_sum не пустой")
    def commission_sum_not_null(self):
        self._tc.assertIsNotNone(self.commission_sum,
                                 f"commission_sum ({self.commission_sum}) пустой" + self.__str__())

    @allure.step("status не пустой")
    def status_not_empty(self):
        self._tc.assertNotEqual(self.status, "",
                                f"status ({self.status}) пустой" + self.__str__())

    @allure.step("operation_time не пустой")
    def operation_time_not_empty(self):
        self._tc.assertNotEqual(self.operation_time, "",
                                f"operation_time ({self.operation_time}) пустой" + self.__str__())

    @allure.step("template_id не пустой")
    def template_id_not_empty(self):
        self._tc.assertNotEqual(self.template_id, "",
                                f"template_id ({self.template_id}) пустой" + self.__str__())


class TransactionParticipant(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.id = data["id"]
        self.pan = data["pan"]
        self.expire = data["expire"]
        self.ps_code = data["ps_code"]
        self.bank_code = data["bank_code"]
        self.owner = data["owner"]

    def check(self, client, **kwargs):
        self.id_not_empty()
        self.pan_not_empty()
        self.ps_code_not_empty()
        self.bank_code_not_empty()
        self.owner_not_empty()

    @allure.step("id не пустой")
    def id_not_empty(self):
        self._tc.assertNotEqual(self.id, "",
                                f"id ({self.id}) пустой" + self.__str__())

    @allure.step("pan не пустой")
    def pan_not_empty(self):
        self._tc.assertNotEqual(self.pan, "",
                                f"pan ({self.pan}) пустой" + self.__str__())

    @allure.step("ps_code не пустой")
    def ps_code_not_empty(self):
        self._tc.assertNotEqual(self.ps_code, "",
                                f"ps_code ({self.ps_code} пустой" + self.__str__())

    @allure.step("bank_code не пустой")
    def bank_code_not_empty(self):
        self._tc.assertNotEqual(self.bank_code, "",
                                f"bank_code ({self.bank_code}) пустой" + self.__str__())

    @allure.step("owner не пустой")
    def owner_not_empty(self):
        self._tc.assertNotEqual(self.owner, "",
                                f"owner ({self.owner}) пустой" + self.__str__())
