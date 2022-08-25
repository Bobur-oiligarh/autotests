import allure

from api_mobile.requests.main_page.cards_balances import CardBalances
from api_mobile.requests.main_page.client_cards import ClientCards
from api_mobile.requests.main_page.client_name import ClientNameRequest
from utils.universal_steps.check_response import check_response


@allure.step("Запрос карт пользователя client_cards")
def step_client_cards(client):
    response = ClientCards(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Запрос балансов по всем картам пользователя client_cards")
def step_all_cards_balances(client):
    response = CardBalances(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("запрос имени пользователя client_name")
def step_get_client_name(client):
    response = ClientNameRequest(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
