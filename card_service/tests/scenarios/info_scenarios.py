import allure

from card_service.tests.steps.info_steps import step_cards_by_phone


@allure.step("Запросы информации по картам пользователя")
def card_info_scenario(context):
    step_cards_by_phone(context)
