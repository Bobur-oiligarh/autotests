import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class SMEAccounts(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.accounts_list: list[SMEAccount] = self.deserialize_to_list_of(SMEAccount, data)

    def check(self, context, **kwargs):
        self.check_list_of("accounts_list", context)

    def set_data_to(self, obj):
        self.set_data_to_obj(obj)

    @allure.step("Установим аккаунты контексту")
    def set_data_to_obj(self, obj):
        obj.accounts = self


class SMEAccount(BaseTypeParent):
    def __init__(self, data: dict):
        super().__init__()
        self.id = data.get("id")
        self.list_id = data.get("list_id")
        self.account_mask = data.get("account_mask")
        self.user_employee = data.get("user_employee")
        self.active = data.get("active")
        self.created_at = data.get("created_at")

    def check(self, context, **kwargs):
        self.assert_not_empty_str("id")
        self.assert_not_empty_str("list_id")
        self.assert_not_empty_str("account_mask")
        self.assert_not_empty_str("user_employee")
        self.assert_not_empty_bool("active")
        self.assert_not_empty_str("created_at")

    def set_data_to(self, obj):
        self.set_account_to(obj)

    @allure.step("Сохраняем аккаунт контексту")
    def set_account_to(self, obj):
        obj.account = self
