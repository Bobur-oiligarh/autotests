import allure

from sme_credits.requests.account.get_accounts import GetAccounts


@allure.step("Get sme/accounts")
def step_sme_accounts(context):
    response = GetAccounts().response()
    response.check_success(context).data.set_data_to(context)
