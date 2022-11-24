import allure

from back_mobile.requests.registration.check_client_registration import CheckClientRegistration

__all__ = [
    "step_check_client_reg"
]


@allure.step("Добавление карты check_client_registration")
def step_check_client_reg(client):
    response = CheckClientRegistration(client).response()
    response.check_success(client).data.set_data_to(client)
