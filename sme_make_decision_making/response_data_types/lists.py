from sme_make_decision_making.response_data_types.accounts import SMEAccounts, SMEAccount
from utils.api_utils.response_data_base import BaseTypeParent


class SMEListAccounts(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.list_accounts: list[SMEAccount] = self.deserialize_to_list_of(SMEAccount, data)

    def check(self, context, **kwargs):
        self.check_list_of("list_accounts", context, **kwargs)

    def set_data_to(self, obj):
        self.set_list_accounts_to(obj)

    def set_list_accounts_to(self, obj):
        obj.list_accounts = self


class SMELists(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.lists: list[SMEList] = self.deserialize_to_list_of(SMEList, data)

    def check(self, context, **kwargs):
        self.check_list_of("lists", context, **kwargs)

    def set_data_to(self, obj):
        self.set_lists_to(obj)

    def set_lists_to(self, obj):
        obj.lists = self


class SMEList(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.list_id = data.get("list_id")
        self.name = data.get("name")
        self.user_employee = data.get("user_employee")
        self.active = data.get("active")
        self.created_at = data.get("created_at")

    def check(self, context, **kwargs):
        self.assert_not_empty_str("list_id")
        self.assert_not_empty_str("name")
        self.assert_not_empty_str("user_employee")
        self.assert_not_empty_bool("active")
        self.assert_not_empty_str("created_at")

    def set_data_to(self, obj):
        self.set_list_to(obj)

    def set_list_to(self, obj):
        obj.list = self
