import allure

from credentials_service.requests.create_user import PostCreateUser
from credentials_service.test_data.credential_service_context import CredentialServiceContext


@allure.step("Запрос на создание пользователя")
def create_user_success(context: CredentialServiceContext):
    response = PostCreateUser(context).response()
    response.check_success(context).data.set_data_to(context)
