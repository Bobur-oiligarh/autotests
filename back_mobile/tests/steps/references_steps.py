import allure

from back_mobile.requests.references.get_atms import GetATMs
from back_mobile.requests.references.get_branches import GetBranches
from back_mobile.requests.references.get_exchange_rates import GetExchangeRates
from back_mobile.requests.references.get_languages import GetLanguages
from back_mobile.requests.references.get_operators import GetOperators


@allure.step("Запрос банкоматов bankomates")
def step_bankomates(context):
    response = GetATMs(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос курсов валют")
def step_exchange_rates(context):
    response = GetExchangeRates(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос филлиалов branches.")
def step_branches(context):
    response = GetBranches(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос доступных языков")
def step_languages(context):
    response = GetLanguages().response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос доступных операторов")
def step_operators(context):
    response = GetOperators().response()
    response.check_success(context).data.set_data_to(context)
