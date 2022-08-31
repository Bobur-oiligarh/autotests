import allure

from api_mobile.tests.steps.p2p_steps import step_p2p_templates, step_p2p_info, step_template_p2p_validate, \
    step_card_p2p_validate, step_p2p_init, step_p2p_confirm


@allure.step("Перевод по шаблону")
def scenario_template_p2p_transaction(client):
    step_p2p_templates(client)
    step_template_p2p_validate(client)
    step_p2p_init(client)
    step_p2p_confirm(client)


@allure.step("Перевод на карту")
def scenario_card_p2p_transaction(client, card_number):
    step_p2p_info(client, card_number)
    step_card_p2p_validate(client)
    step_p2p_init(client)
    step_p2p_confirm(client)
