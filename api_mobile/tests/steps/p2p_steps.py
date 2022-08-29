import allure

from api_mobile.requests.payment.p2p_info import P2PInfo
from api_mobile.requests.payment.p2p_templates import P2PTemplates
from utils.universal_steps.check_response import check_response


@allure.step("Запрос шаблонов переводов templates")
def step_p2p_templates(client):
    response = P2PTemplates(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос информации по карте получателя p2p_info")
def step_p2p_info(client, card_number: str):
    response = P2PInfo(client, card_number).response()
    check_response(response, client)
    response.data.set_data_to(client)
