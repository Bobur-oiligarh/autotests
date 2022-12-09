from unittest import TestCase
from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.scenarios.strategy.check_strategy_methods_work_scenario import \
    check_strategy_methods_work_scenario


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
