from unittest import TestCase

from sme_credits.response_data_types.account.accounts import SMEAccount
from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.check_methods_work_scenario import check_methods_work_scenario
from sme_credits.tests.steps.strategy.step_post_strategy import step_post_strategy


class DemoTestCase(TestCase):
    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.strategy = SMEStrategy(
            data={
                "product_id": "1187",
                "step_id": "A001",
                "user_employee": "RustaM",
                "active": True
            }
        )

    def test_post_strategy(self):
        step_post_strategy(self.context)

#
# class SMETestCase(TestCase):
#
#     def setUp(self) -> None:
#         self.context = SMEContext()
#         self.context.account = SMEAccount({
#             "id": "3655444b-eb68-41f6-9f56-f7e938df8b7f",
#             "account_mask": "15777",
#             "active": True,
#             "list_id": "AL001",
#             "user_employee": "Bobur"
#         })
#
#     def test_get_accounts(self):
#         check_methods_work_scenario(self.context)
