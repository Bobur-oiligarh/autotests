import allure

from card_service.tests.steps.info_steps import cards_by_phone


@allure.step("Запросы информации по картам пользователя")
def card_info_scenario(context):
    cards_by_phone(context)
