import allure

from credentials_service.requests.post_update_user import PostUpdateUser


@allure.step("Запрос на обновление пользователя")
def step_update_user(context):
    response = PostUpdateUser(context).response()
    response.check_success(context).data.set_data_to(context)
