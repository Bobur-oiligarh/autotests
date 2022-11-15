import allure

from card_service.requests.card_methods.get_cards import GetCards


@allure.step("Запрос карт 'GET /v2/cards'")
def step_get_cards(context):
    response = GetCards(context).response()
    response.check_success(context).data.set_data_to(context)

