import allure

from back_mobile.requests.auth.post_login import PostLogin
from back_mobile.requests.auth.post_refreshtoken import PostRefreshToken


@allure.step("Запрос обновления access_token и refresh_token refreshtoken")
def step_refresh_token(context):
    response = PostRefreshToken(context).response()
    response.check_success(context)
    response.data.set_data_to(context)


@allure.step("Аутентификация login")
def step_login(context):
    response = PostLogin(context).response()
    response.check_success(context)
    response.data.set_data_to(context)
