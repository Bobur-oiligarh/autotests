import allure

from sme_credits.requests.strategy.patch_strategy import PatchStrategy


@allure.step("Запрос PATCH/strategies/id, проверка ответа")
def step_patch_strategy(context):
    response = PatchStrategy(context).response()
    response.check_status("Success").check_error_code(0).check_data_is_null()
