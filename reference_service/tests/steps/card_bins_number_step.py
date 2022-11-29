import allure

from reference_service.requests.card_bin.get_card_bins_number import GetCardBinsNumber


@allure.step("Проверка запроса /card-bins/number")
def card_bins_number_success(context):
    response = GetCardBinsNumber(context).response()
    response.check_success(context). \
        data.set_data_to(context)
