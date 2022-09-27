from unittest import TestCase

import allure

from card_service.test_data.card_service_context import CardServiceContext
from card_service.tests.scenarios.info_scenarios import card_info_scenario


class DemoScenarioTestCase(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(phone_number="998941775859")

    def test_main_page(self):
        card_info_scenario(self.context)

        with allure.step(f"{self.context.cards}"):
            pass
