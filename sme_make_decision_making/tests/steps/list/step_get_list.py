import allure

from sme_make_decision_making.requests.list.get_list import GetList
from sme_make_decision_making.requests.list.get_list import GetLists


@allure.step("Запрос Get/list (все листы), проверка ответа")
def step_get_lists(context):
    response = GetLists().response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос GET/list/list_id, проверка ответа")
def step_get_list(context):
    response = GetList(context.list.list_id).response()
    response.check_success(context).data.set_data_to(context)
    return response.data


@allure.step("Запрос листа по id и проверка соответствия")
def step_get_list_assert_equal(context):
    list = step_get_list(context)
    context.list.assert_equal(list)
