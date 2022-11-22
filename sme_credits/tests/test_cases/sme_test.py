from unittest import TestCase
import allure

from sme_credits.response_data_types.accounts_data_type import SMEAccount
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.check_methods_work_scenario import check_methods_work_scenario
from sme_credits.tests.steps.account.delete_accounts_steps import step_delete_sme_accounts
from sme_credits.tests.steps.account.get_accounts_steps import step_get_sme_accounts
from sme_credits.tests.steps.account.patch_accounts_steps import step_patch_account
from sme_credits.tests.steps.account.post_accounts_steps import step_post_sme_accounts


class SMETestCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.account = SMEAccount({
            "id": "3655444b-eb68-41f6-9f56-f7e938df8b7f",
            "account_mask": "15777",
            "active": True,
            "list_id": "AL001",
            "user_employee": "Bobur"
        })

    # def test_get_accounts(self):
    #     step_get_sme_accounts(self.context)
    #
    # def test_post_accounts(self):
    #     step_post_sme_accounts(self.context)
    #
    # def test_delete_accounts(self):
    #     self.context.id = "d1aafa82-70eb-4528-bb63-49ebe67d3152"
    #     step_delete_sme_accounts(self.context)
    #
    # @allure.step("bug")
    # def test_patch_accounts(self):
    #     self.context.id = "fbadbe09-b336-452c-9b70-ec9a0d2907ee"
    #     step_patch_account(self.context)
