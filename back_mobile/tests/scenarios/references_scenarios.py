import allure

from back_mobile.tests.steps.references_steps import step_bankomates, step_languages, step_operators, \
                                                    step_branches, step_exchange_rates


@allure.step("Сценарий запроса данных банкоматов и филиалов")
def scenario_references(client):
    step_bankomates(client)
    step_branches(client)
    step_languages(client)
    step_operators(client)
    step_exchange_rates(client)
