import allure

from back_mobile.requests.main_page.post_cards_balances import PostCardBalances
from back_mobile.requests.main_page.post_cards_operations import PostCardsOperations
from back_mobile.requests.main_page.get_client_cards import GetClientCards
from back_mobile.requests.main_page.get_client_name import GetClientName


@allure.step("Запрос карт пользователя client_cards")
def step_client_cards(context):
    response = GetClientCards(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос балансов по всем картам пользователя client_cards")
def step_all_cards_balances(context):
    response = PostCardBalances(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос имени пользователя client_name")
def step_get_client_name(context):
    response = GetClientName(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос истории операций")
def step_cards_operations(context):
    response = PostCardsOperations(context).response()
    response.check_success(context).data.set_data_to(context)
