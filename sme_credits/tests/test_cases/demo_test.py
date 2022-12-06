from unittest import TestCase

from sme_credits.response_data_types.account.accounts import SMEAccount
from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.check_methods_work_scenario import check_methods_work_scenario
from sme_credits.tests.steps.strategy.step_get_strategies import step_get_strategies
from sme_credits.tests.steps.strategy.step_get_strategy import step_get_strategy
from sme_credits.tests.steps.strategy.step_patch_strategy import step_patch_strategy
from sme_credits.tests.steps.strategy.step_post_strategy import step_post_strategy


class DemoTestCase(TestCase):
    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.strategy = SMEStrategy(
            data={
                "id": "c7f7b99a-555f-4cde-a794-3485c3648b83",
                "product_id": "1187",
                "step_id": "A001",
                "user_employee": "RustaM",
                "active": False
            }
        )

    def test_post_strategy(self):
        step_post_strategy(self.context)

    def test_get_strategies(self):
        step_get_strategies(self.context)

    def test_get_strategy(self):
        step_get_strategy(self.context)

    def test_patch_strategy(self):
        step_patch_strategy(self.context)

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
