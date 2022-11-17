import allure

from sme_credits.requests.account.delete_accounts import DeleteAccounts


@allure.step("Get sme/accounts")
def step_delete_sme_accounts(context, id: str = None):
    context.id = id
    response = DeleteAccounts(context).response()
    response.check_status("Success").check_error_code(0)
