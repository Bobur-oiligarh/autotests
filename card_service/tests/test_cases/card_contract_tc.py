from unittest import TestCase
import allure
from card_service.test_data.card_service_context import CardServiceContext
from card_service.tests.scenarios.info_scenarios import card_contract_scenario


class DemoScenarioTestCase(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(card_number='8600120467515865')

    def test_card_service(self):
        card_contract_scenario(self.context)
        with allure.step(f"{self.context.card_contract}"):
            pass

