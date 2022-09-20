import allure

from back_mobile.requests.registration import FinishRegistration

__all__ = [
    "step_finish_reg"
]


@allure.step("Подтверждение номера телефона finish_registration")
def step_finish_reg(client):
    response = FinishRegistration(client).response()
    response.check_success(response, client)
    response.data.set_data_to(client)
