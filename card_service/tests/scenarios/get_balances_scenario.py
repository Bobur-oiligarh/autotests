import allure

from card_service.tests.steps.get_cards_steps import step_get_cards
from card_service.tests.steps.get_balances_steps import step_get_balance


@allure.step("Запрашиваем карты связанные к данному телефону")
def balances_scenario(context):
    step_get_cards(context)
    step_get_balance(context)
