import allure

from tariff_calculator.requests.post_calculate_p2p_commission import PostCalcP2PCommission


@allure.step("Расчет комиссии для перевода")
def calculate_p2p_commission(context):
    response = PostCalcP2PCommission(context).response()
    response.check_success(context).data.set_data_to(context)
