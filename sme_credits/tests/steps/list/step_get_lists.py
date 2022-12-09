import allure

from sme_credits.requests.list.get_lists import GetLists


@allure.step("Запрос Get/list (все листы), проверка ответа")
def step_get_lists(context):
    response = GetLists().response()
    response.check_success(context).data.set_data_to(context)
