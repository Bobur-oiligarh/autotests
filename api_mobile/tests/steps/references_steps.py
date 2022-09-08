import allure

from api_mobile.requests.references.bankomates import Bancomates
from api_mobile.requests.references.languages import Languages
from utils.universal_steps.check_response import check_response


@allure.step("Запрос банкоматов bankomates")
def step_bankomates(client):
    response = Bancomates(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос доступных языков")
def step_languages(client):
    response = Languages().response()
    check_response(response, client)
    response.data.set_data_to(client)
