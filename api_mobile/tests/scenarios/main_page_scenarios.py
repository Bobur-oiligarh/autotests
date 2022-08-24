import allure

from api_mobile.tests.steps.main_page_steps import step_client_cards


@allure.step("Загрузка главной страницы")
def scenario_open_main_page(client):
    step_client_cards(client)
