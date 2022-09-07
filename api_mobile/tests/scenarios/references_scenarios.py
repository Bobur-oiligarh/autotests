import allure

from api_mobile.tests.steps.references_steps import step_bankomates


@allure.step("Сценарий запроса данных банкоматов и филиалов")
def scenario_atm_branches(client):
    step_bankomates(client)
