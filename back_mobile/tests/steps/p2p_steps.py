import allure

from back_mobile.requests.payment.p2p_confirm import P2PConfirm
from back_mobile.requests.payment.p2p_info import P2PInfo
from back_mobile.requests.payment.p2p_init import P2PInit
from back_mobile.requests.payment.p2p_templates import P2PTemplates
from back_mobile.requests.payment.p2p_validate import P2PValidate
from utils.universal_steps.check_response import check_response


@allure.step("Запрос шаблонов переводов templates")
def step_p2p_templates(client):
    response = P2PTemplates(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос информации по карте получателя p2p_info")
def step_p2p_info(client, card_number: str):
    response = P2PInfo(client, card_number).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Валидация перевода по карте пользователя p2p_validate")
def step_card_p2p_validate(client):
    response = P2PValidate(client, summ=1000, receiver=client.receiver).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Валидация перевода по шаблону p2p_validate")
def step_template_p2p_validate(client):
    response = P2PValidate(client, summ=1000, template=client.templates.templates[0]).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Инициализация перевода p2p_init")
def step_p2p_init(client):
    response = P2PInit(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Подтверждение перевода p2p_confirm")
def step_p2p_confirm(client, confirm_code=""):
    response = P2PConfirm(client, confirm_code).response()
    response.check_success(client).data.set_data_to(client)
