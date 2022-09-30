from unittest import TestCase

import allure

from card_service.test_data.card_service_context import CardServiceContext
from card_service.tests.scenarios.info_scenarios import card_info_scenario, card_contract_scenario


class DemoTestCase1(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(phone_number="998941775859")

    def test_main_page(self):
        card_info_scenario(self.context)

        with allure.step(f"{self.context.cards}"):
            pass


class DemoTestCase2(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(card_number='8600120467515865')

    def test_card_service(self):
        card_contract_scenario(self.context)
        with allure.step(f"{self.context.card_contract}"):
            pass
