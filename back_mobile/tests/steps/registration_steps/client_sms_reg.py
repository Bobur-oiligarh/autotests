import allure

from back_mobile.requests.registration.client_sms_registration import ClientSMSRegistration

__all__ = [
    "step_client_sms_reg"
]


@allure.step("Подтверждение номера карты через СМС client_sms_registration")
def step_client_sms_reg(client):
    response = ClientSMSRegistration(client).response()
    response.check_success(client)\
        .data.set_data_to(client)
