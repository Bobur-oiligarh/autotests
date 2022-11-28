import allure

from credentials_service.requests.post_device_language_update import PostDeviceLangUpdate


@allure.step('Запрос на изменение языка')
def step_device_lang_update(context):
    response = PostDeviceLangUpdate(context).response()
    response.check_status('Success').check_error_code(0).check_error_note("")
