import allure

from back_mobile.requests.main_page.cards_balances import CardBalances
from back_mobile.requests.main_page.cards_operations import CardsOperations
from back_mobile.requests.main_page.client_cards import ClientCards
from back_mobile.requests.main_page.client_name import ClientNameRequest


@allure.step("Запрос карт пользователя client_cards")
def step_client_cards(client):
    response = ClientCards(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос балансов по всем картам пользователя client_cards")
def step_all_cards_balances(client):
    response = CardBalances(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос имени пользователя client_name")
def step_get_client_name(client):
    response = ClientNameRequest(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Запрос истории операций")
def step_cards_operations(client):
    response = CardsOperations(client).response()
    response.check_success(client).data.set_data_to(client)
