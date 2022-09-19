import allure

from back_mobile.requests.auth.login import Login
from back_mobile.requests.auth.refreshtoken import RefreshToken
from utils.universal_steps.check_response import check_response


@allure.step("Запрос обновления access_token и refresh_token refreshtoken")
def step_refresh_token(client):
    response = RefreshToken(client).response()
    check_response(response, client)
    response.data.set_data_to(client)


@allure.step("Аутентификация login")
def step_login(client):
    response = Login(client).response()
    check_response(response, client)
    response.data.set_data_to(client)
