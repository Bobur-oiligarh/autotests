import allure

from api_mobile.requests.registration import StartRegistration, FinishRegistration, GetOffer, AgreeOffer, \
    CheckClientRegistration, ClientSMSRegistration
from utils.universal_steps.check_response import check_response_status


@allure.step("Начало регистрации start_registration")
def step_start_reg(client):
    response = StartRegistration(client).response()
    check_response_status(response)
    response.data.set_sign_id(client)


@allure.step("Подтверждение номера телефона finish_registration")
def step_finish_reg(client):
    response = FinishRegistration(client).response()
    check_response_status(response)
    response.data.set_access_refresh_tokens(client)


@allure.step("Запрос оферты get_offer")
def step_get_offer(client):
    response = GetOffer(client).response()
    check_response_status(response)


@allure.step("Подтверждение оферты agree_offer")
def step_agree_offer(client):
    response = AgreeOffer(client).response()
    check_response_status(response)


@allure.step("Добавление карты check_client_registration")
def step_check_client_reg(client):
    response = CheckClientRegistration(client).response()
    check_response_status(response)
    response.data.set_sign_id_and_confirm_method(client)


@allure.step("Подтверждение номера карты через СМС client_sms_registration")
def step_client_sms_reg(client):
    response = ClientSMSRegistration(client).response()
    check_response_status(response)
    response.data.set_access_refresh_tokens(client)
