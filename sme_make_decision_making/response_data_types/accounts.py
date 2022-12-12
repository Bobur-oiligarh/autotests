from typing import Any

import allure

from utils.api_utils.response_data_base import BaseTypeParent


class SMEAccounts(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.accounts: list[SMEAccount] = self.deserialize_to_list_of(SMEAccount, data)

    def check(self, context, **kwargs):
        self.check_list_of("accounts", context)

    def set_data_to(self, obj):
        self.set_data_to_obj(obj)

    def get_acc_by_param(self, param_name, param_val):
        result = None
        for item in self.accounts:
            if item.__dict__[param_name] == param_val:
                result = item
        return result

    @allure.step("Установим аккаунты контексту")
    def set_data_to_obj(self, obj):
        obj.accounts = self

    @allure.step("Получить аккаунт по параметру {param_name}")
    def get_account_by_param(self, param_name: str, param_value: Any):
        result = None
        for account in self.accounts:
            if account.__dict__[param_name] == param_value:
                result = account
        return result

    @allure.step("Проверяем наличие аккаунта в список аккаунтов")
    def account_exist(self, id: str):
        self._tc.assertTrue(
            True if self.get_account_by_param(param_name="id", param_value=id) else False
        )

    def account_not_exist(self, id: str):
        self._tc.assertFalse(
            False if not self.get_account_by_param(param_name="id", param_value=id) else True
        )


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

    @allure.step("Изменить значение параметра {param_name}")
    def change_param(self, param_name: str, param_value: Any):
        self.__setattr__(param_name, param_value)
