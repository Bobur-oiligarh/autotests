from unittest import TestCase

import allure

from card_service.test_data.card_service_context import CardServiceContext
from card_service.tests.scenarios.get_cards_balance_scenario import cards_balance_scenario
from card_service.tests.scenarios.info_scenarios import card_info_scenario, card_contract_scenario
from card_service.tests.steps.get_cards_steps import step_get_cards


# class DemoTestCase1(TestCase):
#
#     def setUp(self) -> None:
#         self.context = CardServiceContext(phone_number="998941775859")
#
#     def test_main_page(self):
#         card_info_scenario(self.context)
#
#         with allure.step(f"{self.context.cards}"):
#             pass
#
#
# class DemoTestCase2(TestCase):
#
#     def setUp(self) -> None:
#         self.context = CardServiceContext(card_number='8600120467515865')
#
#     def test_card_service(self):
#         card_contract_scenario(self.context)
#         with allure.step(f"{self.context.card_contract}"):
#             pass


class DemoTestCase3(TestCase):

    def setUp(self) -> None:
        self.context = CardServiceContext(
            phone="998941775859",
            bins=["860012", "986016"],
        )

    # def test_get_cards(self):
    #     step_get_cards(self.context)

    def test_get_cards_balance(self):
        cards_balance_scenario(self.context)