import allure

from back_mobile.requests.registration import CheckClientRegistration
from utils.universal_steps.check_response import check_response

__all__ = [
    "step_check_client_reg"
]


@allure.step("Добавление карты check_client_registration")
def step_check_client_reg(client):
    response = CheckClientRegistration(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
