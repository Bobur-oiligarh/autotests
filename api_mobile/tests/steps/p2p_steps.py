import allure

from api_mobile.requests.payment.p2p_templates import P2PTemplates
from utils.universal_steps.check_response import check_response


@allure.step("Запрос шаблонов переводов")
def step_p2p_templates(client):
    response = P2PTemplates(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
