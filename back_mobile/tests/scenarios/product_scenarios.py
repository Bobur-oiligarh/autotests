import allure

from back_mobile.tests.steps.product_steps import step_deposits, step_store_link
from back_mobile.tests.steps.product_steps import step_loans, step_accounts


@allure.step("Сценарий запроса продуктов клиента")
def scenario_products(client):
    step_accounts(client)
    step_loans(client)
    step_deposits(client)
    step_store_link(client)
