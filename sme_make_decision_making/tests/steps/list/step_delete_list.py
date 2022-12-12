import allure

from sme_credits.requests.list.delete_list import DeleteList


@allure.step("Запрос Delete/list/list_id, проверка ответа")
def step_delete_list(context):
    response = DeleteList(context).response()
    response.check_status("Success").check_error_code(0).check_data_is_null()
