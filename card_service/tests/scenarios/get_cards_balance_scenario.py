import allure

from card_service.tests.steps.get_cards_steps import step_get_cards
from card_service.tests.steps.get_cards_balance_steps import step_cards_balance


@allure.step("Запрашиваем карты связанные к данному телефону")
def cards_balance_scenario(context):
    step_get_cards(context)
    step_cards_balance(context)
