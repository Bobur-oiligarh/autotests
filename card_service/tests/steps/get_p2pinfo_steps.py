import allure

from card_service.requests.card_methods.get_p2p_info import GetP2PInfoRequest


@allure.step("Запрос P2P Info и проверяем ответ запроса")
def step_get_p2p_info(context):
    response = GetP2PInfoRequest(context).response()
    response.check_success().data.set_data_to(context)
