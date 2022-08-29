import allure

from api_mobile.tests.steps.p2p_steps import step_p2p_templates


@allure.step("Перевод по шаблону")
def scenario_template_p2p_transaction(client):
    step_p2p_templates(client)
