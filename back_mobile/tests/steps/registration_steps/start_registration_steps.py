import allure

from back_mobile.requests.registration import StartRegistration
from back_mobile.test_data.client import Client

__all__ = [
    "step_start_reg_success",
    "step_start_reg_empty_phone",
    "step_start_reg_empty_phone_type",
    "step_start_reg_unsupported_version"
]


@allure.step("Начало регистрации start_registration")
def step_start_reg_success(client: Client):
    response = StartRegistration(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Начало регистрации start_registration")
def step_start_reg_unsupported_version(client: Client):
    client.app_version = "1.0.0"
    response = StartRegistration(client).response()
    response.check_failure("Failure", 1027,
                           "Эта версия приложения теперь не поддерживается.Обновите приложение")


@allure.step("Начало регистрации start_registration")
def step_start_reg_empty_phone(client: Client):
    client.user.phone_number = ""
    response = StartRegistration(client).response()
    response.check_failure("Failure", -70,
                           "Key: 'reqStartReg.Phone' Error:Field validation for 'Phone' failed on the 'required' tag")


@allure.step("Начало регистрации start_registration")
def step_start_reg_empty_phone_type(client: Client):
    client.device.phone_type = ""
    response = StartRegistration(client).response()
    response.check_failure("Failure", -70,
                           "Key: 'reqStartReg.PhoneType' "
                           "Error:Field validation for 'PhoneType' failed on the 'required' tag")
