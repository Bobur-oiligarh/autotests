import allure
from sme_credits.requests.strategy.get_all_strategies import GetStrategies


@allure.step("Запрос Get/strategies, проверка ответа")
def step_get_strategies(context):
    response = GetStrategies().response()
    response.check_success(context).data.set_data_to(context)

