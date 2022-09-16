import allure

from api_mobile.requests.references.bankomates import Bancomates
from api_mobile.requests.references.branches import Branches
from api_mobile.requests.references.exchange_rates import ExchangeRateRequest
from api_mobile.requests.references.languages import Languages
from api_mobile.requests.references.operators import Operators
from utils.universal_steps.check_response import check_response


@allure.step("Запрос банкоматов bankomates")
def step_bankomates(client):
    response = Bancomates(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос курсов валют")
def step_exchange_rates(client):
    response = ExchangeRateRequest(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос филлиалов branches.")
def step_branches(client):
    response = Branches(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос доступных языков")
def step_languages(client):
    response = Languages().response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос доступных операторов")
def step_operators(client):
    response = Operators().response()
    check_response(response, client)
    response.data.set_data_to(client)
