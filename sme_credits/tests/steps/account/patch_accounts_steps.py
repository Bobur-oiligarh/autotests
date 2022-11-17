import allure

from sme_credits.requests.account.patch_accounts import PatchAccounts


@allure.step("Запрос PATCH accounts/{id}, проверка ответа")
def step_patch_account(context):
    response = PatchAccounts(context).response()
    response.check_status("Success").check_error_code(0)
