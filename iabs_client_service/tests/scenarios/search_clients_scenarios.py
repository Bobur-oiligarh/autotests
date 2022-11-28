import allure

from iabs_client_service.tests.steps.get_clients_search_steps import step_search_clients


@allure.step("Сценарий запроса IABS клиента")
def scenario_search_clients(context):
    step_search_clients(context)
