import allure

from card_service.requests.get_cards_by_phone import GetCardsByPhone


@allure.step("Запрос карт по номеру телефона cards_by_number")
def step_cards_by_phone(context):
    response = GetCardsByPhone(context).response()
    response.check_success(context).data.set_data_to(context)
