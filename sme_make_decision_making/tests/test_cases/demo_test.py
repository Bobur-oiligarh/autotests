from unittest import TestCase

from sme_make_decision_making.response_data_types.criterions import SMECriterion
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_118_scenario import vbnv_118_scenario


class DemoTest(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.criterion = SMECriterion(
            {
                "active": True,
                "amount_check": 1111,
                "count_check": 44,
                "date_action": 2,
                "date_check": 365,
                "id": "R299",
                "list_id": "",
                "name": "Наличие левого полужопия",
                "points": 0,
                "step_id": "A001",
                "user_employee": "Ivan"
            }
        )

    def test_criterions(self):
        vbnv_118_scenario(self.context)
