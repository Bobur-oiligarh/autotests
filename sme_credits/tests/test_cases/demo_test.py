from unittest import TestCase
from parameterized import parameterized
from sme_credits.response_data_types.account.accounts import SMEAccount
from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.account.check_methods_work_scenario import check_methods_work_scenario
from sme_credits.tests.scenarios.strategy.check_strategy_methods_work_scenario import \
    check_strategy_methods_work_scenario
from sme_credits.tests.steps.strategy.step_delete_strategy import step_delete_strategy
from sme_credits.tests.steps.strategy.step_get_strategies import step_get_strategies
from sme_credits.tests.steps.strategy.step_get_strategy import step_get_strategy
from sme_credits.tests.steps.strategy.step_patch_strategy import step_patch_strategy
from sme_credits.tests.steps.strategy.step_post_strategy import step_post_strategy


class DemoTestCase(TestCase):
    step_id_params = ["A001", "A002", "B002"]

    def setUp(self) -> None:
        self.context = SMEContext()
        for step_id in self.step_id_params:
            self.context.strategy = SMEStrategy(
                data={
                    "product_id": "1187",
                    "step_id": step_id,
                    "user_employee": "Boxodir",
                    "active": True
                }
            )

    def test_methods_work(self):
        check_strategy_methods_work_scenario(self.context)


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

#     def test_get_accounts(self):
#         check_methods_work_scenario(self.context)
