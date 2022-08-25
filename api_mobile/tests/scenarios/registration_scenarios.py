import allure

from api_mobile.tests.steps.identification_steps import set_sms_code
from api_mobile.tests.steps.registration_steps import step_client_sms_reg, step_check_client_reg, step_agree_offer, \
    step_get_offer, step_finish_reg, step_start_reg


@allure.step("Процесс регистрации")
def scenario_registration(client):
    step_start_reg(client)
    set_sms_code(client)
    step_finish_reg(client)
    step_get_offer(client)
    step_agree_offer(client)
    step_check_client_reg(client)
    set_sms_code(client)
    step_client_sms_reg(client)
