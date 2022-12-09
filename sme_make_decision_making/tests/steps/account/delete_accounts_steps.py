import allure

from sme_make_decision_making.requests.account.delete_accounts import DeleteAccounts


@allure.step("Get sme/accounts")
def step_delete_sme_accounts(context):
    response = DeleteAccounts(context).response()
    response.check_status("Success").check_error_code(0)
