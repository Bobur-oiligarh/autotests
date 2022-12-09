from unittest import TestCase

from sme_make_decision_making.response_data_types.accounts import SMEAccount
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_100_scenario import vbnv_100_scenario


class VBNV100TestCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.account = SMEAccount({
            "id": "3655444b-eb68-41f6-9f56-f7e938df8b7f",
            "account_mask": "15777",
            "active": True,
            "list_id": "AL001",
            "user_employee": "Bobur"
        })

    def test_accounts(self):
        vbnv_100_scenario(self.context)
