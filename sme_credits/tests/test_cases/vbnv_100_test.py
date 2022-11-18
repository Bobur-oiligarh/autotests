from unittest import TestCase

from sme_credits.response_data_types.accounts_data_type import SMEAccount
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.check_methods_work_scenario import check_methods_work_scenario


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

    def test_get_accounts(self):
        check_methods_work_scenario(self.context)
