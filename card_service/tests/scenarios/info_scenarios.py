import allure

from card_service.tests.steps.info_steps import cards_by_phone


@allure.step("Запросы информации по картам пользователя")
def card_info_scenario(client):
    cards_by_phone(client)
