from unittest import TestCase

from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.demo_scenarios import demo_criterion_scenario
from sme_make_decision_making.tests.steps.criterions.get_criterions_steps import get_criterions


class DemoTest(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()

    def test_criterions(self):
        demo_criterion_scenario(self.context)