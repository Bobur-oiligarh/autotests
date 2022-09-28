import allure

from card_service.tests.steps.card_contract_steps import step_get_and_check_card_contract
from card_service.tests.steps.info_steps import cards_by_phone
from card_service.tests.steps.info_steps import step_cards_by_phone


@allure.step("Запрос информации по картам пользователя")
def card_info_scenario(context):
    step_cards_by_phone(context)


@allure.step("Запрос контракта для карты по его номеру")
def card_contract_scenario(context):
    step_get_and_check_card_contract(context)
