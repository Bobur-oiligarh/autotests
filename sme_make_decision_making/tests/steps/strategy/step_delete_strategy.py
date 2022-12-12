import allure

from sme_make_decision_making.requests.strategy.delete_strategy import DeleteStrategy


@allure.step("Запрос DELETE/strategy/id, проверка ответа")
def step_delete_strategy(context):
    response = DeleteStrategy(context).response()
    response.check_status("Success").check_error_code(0).check_data_is_null()
