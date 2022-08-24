import allure

from api_mobile.requests.main_page.client_cards import ClientCards
from utils.universal_steps.check_response import check_response


@allure.step("Запрос карт пользователя client_cards")
def step_client_cards(client):
    response = ClientCards(client).response()
    check_response(response, client)
    response.data.set_cards(client)
