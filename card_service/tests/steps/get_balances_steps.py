import allure

from card_service.requests.card_methods.get_balances import GetBalances


@allure.step("Запрос 'GET /v2/balances'")
def step_get_balance(context):
    response = GetBalances(context).response()
    response.check_success(context).data.set_data_to(context)
