import allure

from card_service.requests.card_methods.get_cards_balance import CardsBalanceRequest


@allure.step("Запрос 'GET /v2/balances'")
def step_cards_balance(context):
    response = CardsBalanceRequest(context).response()
    response.check_success(context).data.set_data_to(context)
