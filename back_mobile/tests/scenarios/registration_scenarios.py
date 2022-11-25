import allure

from back_mobile.tests.steps.identification_steps import set_sms_code
from back_mobile.tests.steps.registration_steps.agree_offer_steps import step_agree_offer
from back_mobile.tests.steps.registration_steps.check_client_reg_steps import step_check_client_reg
from back_mobile.tests.steps.registration_steps.client_sms_reg import step_client_sms_reg
from back_mobile.tests.steps.registration_steps.finish_registration_steps import step_finish_reg
from back_mobile.tests.steps.registration_steps.get_offer_steps import step_get_offer
from back_mobile.tests.steps.registration_steps.start_registration_steps import step_start_reg_success


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
