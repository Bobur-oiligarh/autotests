import allure

from back_mobile.tests.steps.identification_steps import set_sms_code
from back_mobile.tests.steps.p2p_steps import step_p2p_templates, step_p2p_info, step_template_p2p_validate, \
    step_card_p2p_validate, step_p2p_init, step_p2p_confirm


@allure.step("Перевод по шаблону")
def scenario_template_p2p_transaction(client):
    step_p2p_templates(client)
    step_template_p2p_validate(client)
    step_p2p_init(client)
    if client.p2p_validate_result.is_confirm:
        set_sms_code(client)
    step_p2p_confirm(client, client.code)


@allure.step("Перевод на карту")
def scenario_card_p2p_transaction(client, card_number: str):
    step_p2p_info(client, card_number)
    step_card_p2p_validate(client)
    step_p2p_init(client)
    if client.p2p_validate_result.is_confirm:
        set_sms_code(client)
    step_p2p_confirm(client, client.code)
