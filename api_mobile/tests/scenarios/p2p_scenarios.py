import allure

from api_mobile.tests.steps.p2p_steps import step_p2p_templates, step_p2p_info


@allure.step("Перевод по шаблону")
def scenario_template_p2p_transaction(client):
    step_p2p_templates(client)


@allure.step("Перевод на карту")
def scenario_card_p2p_transaction(client, card_number):
    step_p2p_info(client, card_number)
