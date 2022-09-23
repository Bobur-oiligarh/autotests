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
        self.check_all_accounts(client, **kwargs)

    @allure.step("Проверк всех счетов клиента")
    def check_all_accounts(self, client, **kwargs):
        for acc in self.accounts:
            with allure.step(f"Проверка параметров счета {acc.name_acc}"):
                acc.check(client, **kwargs)


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
        self.assert_not_empty("name_acc")
        self.assert_not_empty("account")
        self.assert_not_empty("code_currency")
        self.assert_not_empty("saldo")
        self.assert_not_empty("code_filial")
        self.assert_not_empty("code_coa")
        self.assert_not_empty("condition")
        self.assert_not_empty("create_date")
        self.assert_not_empty("id")
