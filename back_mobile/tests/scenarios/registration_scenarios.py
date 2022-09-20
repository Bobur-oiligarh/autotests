import allure

from back_mobile.tests.steps.identification_steps import set_sms_code
from back_mobile.tests.steps import *


@allure.step("Процесс регистрации")
def scenario_registration(client):
    step_start_reg_success(client)
    set_sms_code(client)
    step_finish_reg(client)
    step_get_offer(client)
    step_agree_offer(client)
    step_check_client_reg(client)
    set_sms_code(client)
    step_client_sms_reg(client)
