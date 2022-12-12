import allure

from sme_make_decision_making.requests.strategy.get_strategy import GetStrategy


@allure.step("Запрос GET/strategies/id, проверка ответа")
def step_get_strategy(context):
    response = GetStrategy(context.strategy.id).response()
    response.check_success(context)
    return response.data


@allure.step("Запрос strategy по его id и его сопоставление")
def step_get_strategy_check_equal(context):
    strategy = step_get_strategy(context)
    strategy.assert_equal(context.strategy)
