import allure

from credentials_service.requests import CreateUser
from credentials_service.test_data.credential_service_context import CredentialServiceContext

__all__ = [
    "create_user_success"
]


@allure.step("Запрос на создание пользователя")
def create_user_success(context: CredentialServiceContext):
    response = CreateUser(context).response()
    response.check_success(context).data.set_data_to(context)
