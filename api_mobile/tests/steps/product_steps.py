import allure

from api_mobile.requests.product.branches import Accounts
from api_mobile.requests.product.deposits import Deposits
from api_mobile.requests.product.loans import Loans
from utils.universal_steps.check_response import check_response


@allure.step("Запрос кредитов клиента loans")
def step_loans(client):
    response = Loans(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос счетов клиента accounts")
def step_accounts(client):
    response = Accounts(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос депозитов клиента deposits")
def step_deposits(client):
    response = Deposits(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
