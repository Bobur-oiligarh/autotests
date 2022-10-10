import allure

from credentials_service.requests.get_device_info_request import GetDeviceInfo


@allure.step('Запрашиваем инфо по девайсу')
def step_get_and_check_device_info(context):
    response = GetDeviceInfo(context).response()
    response.check_success(context).data.set_data_to(context)
