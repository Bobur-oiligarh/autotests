import allure

from back_mobile.tests.steps.main_page_steps import step_client_cards, step_all_cards_balances, step_get_client_name, \
    step_cards_operations


@allure.step("Загрузка главной страницы")
def scenario_open_main_page(client):
    step_client_cards(client)
    step_all_cards_balances(client)
    step_get_client_name(client)
    step_cards_operations(client)
