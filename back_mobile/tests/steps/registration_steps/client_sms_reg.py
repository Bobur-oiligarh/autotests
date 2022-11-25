import allure

from back_mobile.requests.registration.post_client_sms_reg import PostClientSMSRegistration


@allure.step("Подтверждение номера карты через СМС client_sms_registration")
def step_client_sms_reg(context):
    response = PostClientSMSRegistration(context).response()
    response.check_success(context)\
        .data.set_data_to(context)
