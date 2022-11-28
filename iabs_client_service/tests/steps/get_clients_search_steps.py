import allure

from iabs_client_service.requests.get_clients_search import GetIABSClientById


@allure.step("Запрос на получения клиента IABS")
def step_search_clients(context):
    response = GetIABSClientById(context).response()
    response.check_success(context).data.set_data_to(context)

