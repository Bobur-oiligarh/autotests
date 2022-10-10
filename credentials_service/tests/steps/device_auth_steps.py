import allure

from credentials_service.requests.device_auth_requests import DeviceAuthRequest


@allure.step('Запрос на аутентификацию девайса, проверяем ответ')
def step_device_auth(context):
    response = DeviceAuthRequest(context).response()
    response.check_success(context).data.set_data_to(context)

