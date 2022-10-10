import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = [
    "OpenedAccounts",
    "Account"
]


class OpenedAccounts(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.accounts: list[Account] = self.deserialize_to_list_of(Account, data)

    def set_data_to(self, obj):
        self.set_accounts_to_client(obj)

    @allure.step("Установить счета клиенту")
    def set_accounts_to_client(self, client):
        client.accounts = self

    def check(self, client, **kwargs):
        self.check_list_of("accounts", client, **kwargs)


class Account(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.name_acc = data["name_acc"]
        self.account = data["account"]
        self.code_currency = data["code_currency"]
        self.saldo = data["saldo"]
        self.code_filial = data["code_filial"]
        self.code_coa = data["code_coa"]
        self.condition = data["condition"]
        self.create_date = data["create_date"]
        self.id = data["id"]

    def check(self, client, **kwargs):
        self.assert_not_empty_str("name_acc")
        self.assert_not_empty_str("account")
        self.assert_not_empty_str("code_currency")
        self.assert_not_empty_str("saldo")
        self.assert_not_empty_str("code_filial")
        self.assert_not_empty_str("code_coa")
        self.assert_not_empty_str("condition")
        self.assert_not_empty_str("create_date")
        self.assert_not_empty_str("id")
