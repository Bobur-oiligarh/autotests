import allure

from card_service.requests.cards_by_phone import CardsByPhone


@allure.step("Запрос карт по номеру телефона cards_by_number")
def step_cards_by_phone(context):
    response = CardsByPhone(context).response()
    response.check_success(context).data.set_data_to(context)
