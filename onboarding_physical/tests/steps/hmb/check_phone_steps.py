import allure

from onboarding_physical.requests.hmb.get_check_phone import GetCheckPhone


@allure.step('Делаем запрос инфо о телефоне и проверяем его')
def step_check_phone(context):
    response = GetCheckPhone().response()
    response.check_status("Success").check_error_code(0).check_error_note("").check_data_not_null()
    response.data.set_data_to(context)


