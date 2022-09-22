import allure

from reference_service.requests.card_bin.card_bins_number import CardBinsNumber


@allure.step("Проверка запроса /card-bins/number")
def card_bins_number_success(context):
    response = CardBinsNumber(context).response()
    response.check_success(context). \
        data.set_data_to(context)
