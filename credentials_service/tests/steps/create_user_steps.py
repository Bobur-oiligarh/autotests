import allure

from credentials_service.requests.post_create_user import PostCreateUser


@allure.step("Запрос на создание пользователя")
def create_user_success(context):
    response = PostCreateUser(context).response()
    response.check_success(context).data.set_data_to(context)
