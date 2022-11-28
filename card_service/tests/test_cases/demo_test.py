from unittest import TestCase

import allure

from card_service.test_data.card_service_context import CardServiceContext
from card_service.tests.scenarios.balances_scenario import balances_scenario
from card_service.tests.steps.get_cards_steps import step_get_cards
from card_service.tests.steps.get_p2pinfo_steps import step_get_p2p_info


class DemoTestCase(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(
            phone="998941775859",
            bins=["860012", "986016"],
            card_number="8600120480409831"
        )

    @allure.step("Запрос карт")
    def test_get_cards(self):
        step_get_cards(self.context)

    def test_get_balances(self):
        balances_scenario(self.context)

    def test_get_p2p_info(self):
        step_get_p2p_info(self.context)
