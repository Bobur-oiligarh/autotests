import allure

from card_service.requests.cards_by_phone import CardsByPhone
from utils.universal_steps.check_response import check_response


@allure.step("Запрос карт по номеру телефона cards_by_number")
def cards_by_phone(client):
    response = CardsByPhone(client.get_by_name("phone_number")).response()
    check_response(response, client)
    response.data.set_data_to(client)
