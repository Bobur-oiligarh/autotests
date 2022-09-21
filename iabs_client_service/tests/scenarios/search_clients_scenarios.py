import allure

from iabs_client_service.tests.steps.search_clients_steps import step_iabs_client_by_id


@allure.step("Сценарий запроса IABS клиента")
def scenario_search_clients(client_uid):
    step_iabs_client_by_id(client_uid)
