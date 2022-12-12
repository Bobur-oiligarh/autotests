import allure
from sme_credits.requests.list.patch_list import PatchList


@allure.step("Запрос PATCH/list/list_id, проверка ответа")
def step_patch_list(context):
    response = PatchList(context).response()
    response.check_status("Success").check_error_code(0).check_data_is_null()
