import allure

from sme_credits.requests.list.get_list import GetList


@allure.step("Запрос GET/list/list_id, проверка ответа")
def step_get_list(context):
    response = GetList(context).response()
    response.check_success(context).data.set_data_to(context)
