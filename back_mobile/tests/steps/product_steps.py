import allure

from back_mobile.requests.product.accounts import Accounts
from back_mobile.requests.product.deposits import Deposits
from back_mobile.requests.product.loans import Loans
from back_mobile.requests.product.store_link import StoreLink


@allure.step("Запрос кредитов клиента loans")
def step_loans(client):
    response = Loans(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос счетов клиента accounts")
def step_accounts(client):
    response = Accounts(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос депозитов клиента deposits")
def step_deposits(client):
    response = Deposits(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос ссылки на HamkorStore")
def step_store_link(client):
    response = StoreLink(client).response()
    response.check_success(client).data.set_data_to(client)
