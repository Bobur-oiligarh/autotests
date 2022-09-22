import allure

from iabs_client_service.requests.search_clients import IABSClientByIdRequest
from utils.universal_steps.check_response import check_response


@allure.step("Запрос на получения клиента IABS")
def step_search_clients(context):
    response = IABSClientByIdRequest(context).response()
    check_response(response, context)
    response.data.set_data_to(context)

