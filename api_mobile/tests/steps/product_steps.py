import allure

from api_mobile.requests.product.loans import Loans
from utils.universal_steps.check_response import check_response


@allure.step("Запрос кредитов клиента loans")
def step_loans(client):
    response = Loans(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
