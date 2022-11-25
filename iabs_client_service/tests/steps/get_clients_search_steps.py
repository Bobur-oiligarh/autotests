import allure

from iabs_client_service.requests import IABSClientByIdRequest

__all__ = ['step_search_clients']


@allure.step("Запрос на получения клиента IABS")
def step_search_clients(context):
    response = IABSClientByIdRequest(context).response()
    response.check_success(context).data.set_data_to(context)

