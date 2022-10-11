import allure

from onboarding_physical.requests.hmb.check_prospect_by_client_id_requests import CheckProspectByClientID


@allure.step("Запрашиваем prospect по clientID и проверяем ответ")
def step_check_prospect(context):
    response = CheckProspectByClientID(context).response()
    response.check_success(context).data.set_data_to(context)