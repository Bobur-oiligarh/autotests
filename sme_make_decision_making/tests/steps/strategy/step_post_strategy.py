import allure

from sme_make_decision_making.requests.strategy.post_strategy import PostStrategy


@allure.step("Запрос POST/strategies, проверка параметров ответа")
def step_post_strategy(context):
    response = PostStrategy(context).response()
    response.check_success(context).data.set_data_to(context)
