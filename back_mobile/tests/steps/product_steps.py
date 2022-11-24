import allure

from back_mobile.requests.product.get_accounts import GetAccounts
from back_mobile.requests.product.get_deposits import GetDeposits
from back_mobile.requests.product.get_loans import GetLoans
from back_mobile.requests.product.get_store_link import GetStoreLink


@allure.step("Запрос кредитов клиента loans")
def step_loans(context):
    response = GetLoans(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос счетов клиента accounts")
def step_accounts(context):
    response = GetAccounts(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос депозитов клиента deposits")
def step_deposits(context):
    response = GetDeposits(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос ссылки на HamkorStore")
def step_store_link(context):
    response = GetStoreLink(context).response()
    response.check_success(context).data.set_data_to(context)
