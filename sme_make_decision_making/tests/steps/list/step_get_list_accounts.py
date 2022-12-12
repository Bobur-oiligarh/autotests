import allure

from sme_make_decision_making.requests.list.get_list_accounts import GetListAccounts


@allure.step("Запрос Get/list/:id/accounts, проверка ответа")
def step_get_list_accounts(context):
    response = GetListAccounts(context).response()
    response.check_success(context).data.set_data_to(context)
