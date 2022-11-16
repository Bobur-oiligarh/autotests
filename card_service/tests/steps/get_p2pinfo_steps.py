import allure

from card_service.requests.card_methods.get_p2p_info import GetP2PInfo


@allure.step("Запрос P2P Info и проверяем ответ запроса")
def step_get_p2p_info(context):
    response = GetP2PInfo(context).response()
    response.check_success(context).data.set_data_to(context)
