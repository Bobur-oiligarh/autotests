import allure

from api_mobile.tests.steps.references_steps import step_bankomates, step_languages


@allure.step("Сценарий запроса данных банкоматов и филиалов")
def scenario_references(client):
    step_bankomates(client)
    step_languages(client)