import allure

from api_mobile.response_data_types.response_data_base import BaseType, BaseTypeParent


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
        self.name_acc_not_empty()
        self.account_not_empty()
        self.code_currency_not_empty()
        self.saldo_not_empty()
        self.code_filial_not_empty()
        self.code_coa_not_empty()
        self.condition_not_empty()
        self.create_date_not_empty()
        self.id_not_empty()

    @allure.step("name_acc не пустой")
    def name_acc_not_empty(self):
        self._tc.assertNotEqual(self.name_acc, "",
                                f"name_acc ({self.name_acc}) пустой" + self.__str__())

    @allure.step("account не пустой")
    def account_not_empty(self):
        self._tc.assertNotEqual(self.account, "",
                                f"account ({self.account}) пустой" + self.__str__())

    @allure.step("code_currency не пустой")
    def code_currency_not_empty(self):
        self._tc.assertNotEqual(self.code_currency, "",
                                f"code_currency ({self.code_currency}) пустой" + self.__str__())

    @allure.step("saldo не пустой")
    def saldo_not_empty(self):
        self._tc.assertNotEqual(self.saldo, "",
                                f"saldo ({self.saldo}) пустой" + self.__str__())

    @allure.step("code_filial не пустой")
    def code_filial_not_empty(self):
        self._tc.assertNotEqual(self.code_filial, "",
                                f"code_filial ({self.code_filial}) пустой" + self.__str__())

    @allure.step("code_coa не пустой")
    def code_coa_not_empty(self):
        self._tc.assertNotEqual(self.code_coa, "",
                                f"code_coa ({self.code_coa}) пустой" + self.__str__())

    @allure.step("condition не пустой")
    def condition_not_empty(self):
        self._tc.assertNotEqual(self.condition, "",
                                f"condition ({self.condition}) пустой" + self.__str__())

    @allure.step("create_date не пустой")
    def create_date_not_empty(self):
        self._tc.assertNotEqual(self.create_date, "",
                                f"create_date ({self.create_date}) пустой" + self.__str__())

    @allure.step("id не пустой")
    def id_not_empty(self):
        self._tc.assertNotEqual(self.id, "",
                                f"id ({self.id}) пустой" + self.__str__())
