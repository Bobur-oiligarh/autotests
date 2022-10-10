import allure

from credentials_service.requests.device_language_update_requests import DeviceLangUpdateRequest


@allure.step('Запрос на изменение языка')
def step_device_lang_update(context):
    response = DeviceLangUpdateRequest(context).response()
    response.check_status('Success').check_error_code(0).check_error_note("")  # Проверим базовые параметры
                                                                               # в ответе запроса, а data = null
