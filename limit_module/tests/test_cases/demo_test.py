import allure
from unittest import TestCase

from limit_module.test_data.limit_module_context import LimitModuleContext
from limit_module.tests.steps.p2p_all_limit_steps import step_p2p_all_limit


class LimitModuleTestCase(TestCase):

    def setUp(self) -> None:
        self.context = LimitModuleContext(
            product_id="p2p",
            iabs_id="4959379",
            limit_types=["DAILY_SUM", "MONTHLY_SUM"]
        )

    def test_limit_module(self):
        step_p2p_all_limit(self.context)

        with allure.step(f"{self.context.limits}"):
            pass
