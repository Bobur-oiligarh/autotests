import allure

from iabs_client_service.requests.post_clients_search_requests import PostClientsSearch


@allure.step('Делаем POST запрос на clients/search и проверяем ответ')
def step_clients_search(context):
    response = PostClientsSearch(context).response()
    response.check_success(context).data.set_data_to(context)
