import allure

from back_mobile.requests.registration import ClientSMSRegistration
from utils.universal_steps.check_response import check_response

__all__ = [
    "step_client_sms_reg"
]


@allure.step("Подтверждение номера карты через СМС client_sms_registration")
def step_client_sms_reg(client):
    response = ClientSMSRegistration(client).response()
    response.check_success(client)\
        .data.set_data_to(client)
