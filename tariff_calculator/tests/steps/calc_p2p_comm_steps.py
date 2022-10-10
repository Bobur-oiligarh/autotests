import allure

from tariff_calculator.requests.calculate_p2p_commission import CalcP2PCommission


@allure.step("Расчет комиссии для перевода")
def calculate_p2p_commission(context):
    response = CalcP2PCommission(context).response()
    response.check_success(context).data.set_data_to(context)
