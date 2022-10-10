import allure

from credentials_service.requests import UpdateUser
from credentials_service.test_data.credential_service_context import CredentialServiceContext

__all__ = [
    "step_update_user"
]


@allure.step("Запрос на обновление пользователя")
def step_update_user(context: CredentialServiceContext):
    response = UpdateUser(context).response()
    response.check_success(context).data.set_data_to(context)
