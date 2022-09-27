import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "Templates",
    "Template",
    "TransactionParticipant"
]


class Templates(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.templates: list = self.deserialize_to_list_of(Template, data)

    def set_data_to(self, obj):
        self._set_templates_to_client(obj)

    @allure.step("Установить шаблоны")
    def _set_templates_to_client(self, client):
        client.templates = self

    @allure.step("Проверка всех шаблонов")
    def check(self, client, **kwargs):
        self.check_list_of("templates", client, **kwargs)


class Template(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.sender = TransactionParticipant(data["sender"])
        self.receiver = TransactionParticipant(data["receiver"])
        self.sum: float = data["sum"]
        self.commission_sum: float = data["commission_sum"]
        self.status = data["status"]
        self.operation_time = data["operation_time"]
        self.template_id = data["template_id"]

    def check(self, client, **kwargs):
        self.check_attrs_of("sender", client, **kwargs)
        self.check_attrs_of("receiver", client, **kwargs)
        self.assert_not_none("sum")
        self.assert_not_none("commission_sum")
        self.assert_not_none("status")
        self.assert_not_none("operation_time")
        self.assert_not_none("template_id")


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
        self.assert_not_empty("id")
        self.assert_not_empty("pan")
        self.assert_not_none("expire")
        self.assert_not_empty("ps_code")
        self.assert_not_empty("bank_code")
        self.assert_not_empty("owner")
