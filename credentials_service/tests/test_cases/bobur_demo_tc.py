from unittest import TestCase
import allure
from credentials_service.test_data.credential_service_context import CredentialServiceContext
from credentials_service.tests.steps.device_auth_steps import step_device_auth
from credentials_service.tests.steps.get_device_info_steps import step_get_and_check_device_info


class CredentialServiceTestCases(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            device_id='string',
            user_id='b58c689d-845b-4503-a77f-6f1b316a52d9'
            )
        self.context.refresh_token = '0eb7ca77-9427-3611-8ecc-bf24f5a7d82b'

    @allure.description('Проверка запрроса девайс аутентифакацию')
    def test_get_device_info(self):
        step_get_and_check_device_info(self.context)
        step_device_auth(self.context)

