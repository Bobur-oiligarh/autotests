import allure

from credentials_service.requests.post_device_auth import PostDeviceAuth


@allure.step('Запрос на аутентификацию девайса, проверяем ответ')
def step_device_auth(context):
    response = PostDeviceAuth(context).response()
    response.check_success(context).data.set_data_to(context)

