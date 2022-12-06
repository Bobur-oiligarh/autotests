import allure

from sme_credits.requests.strategy.get_strategy import GetStrategy


@allure.step("Запрос GET/strategies/id, проверка ответа")
def step_get_strategy(context):
    response = GetStrategy(context).response()
    response.check_success(context).data.set_data_to(context)
