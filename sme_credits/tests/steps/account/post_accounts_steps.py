import allure

from sme_credits.requests.account.post_accounts import PostAccounts


@allure.step("Делаем запрос POST /accounts")
def step_post_sme_accounts(context):
    response = PostAccounts(context).response()
    response.check_success(context).data.set_data_to(context)
