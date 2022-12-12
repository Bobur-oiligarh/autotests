from unittest import TestCase
from parameterized import parameterized
from sme_make_decision_making.response_data_types.accounts import SMEAccount
from sme_make_decision_making.response_data_types.criterions import SMECriterion
from sme_make_decision_making.response_data_types.lists import SMEList
from sme_make_decision_making.response_data_types.strategies import SMEStrategy
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_100_scenario import vbnv_100_scenario
from sme_make_decision_making.tests.scenarios.vbnv_116_scenario import vbnv_116_scenario
from sme_make_decision_making.tests.scenarios.vbnv_119_scenario import vbnv_119_scenario
from sme_make_decision_making.tests.scenarios.vbnv_118_scenario import vbnv_118_scenario


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
        vbnv_119_scenario(self.context)


class SMEAccountTestCase(TestCase):

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
#         vbnv_100_scenario(self.context)


class DemoCriterionTest(TestCase):

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

    # def test_criterions(self):
    #     vbnv_118_scenario(self.context)


class DemoListCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.list = SMEList(
            data={
                "list_id": "33334",
                "name": "C1",
                "user_employee": "Xamdam",
                "active": True
            }
        )

    def test_vbnv_116(self):
        vbnv_116_scenario(self.context)
