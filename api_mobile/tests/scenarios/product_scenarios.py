import allure

from api_mobile.tests.steps.product_steps import step_loans


@allure.step("Сценарий запроса продуктов клиента")
def scenario_products(client):
    step_loans(client)
