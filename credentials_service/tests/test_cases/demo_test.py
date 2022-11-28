from unittest import TestCase
import allure
from credentials_service.test_data.credential_service_context import CredentialServiceContext
from credentials_service.tests.steps.create_user_steps import create_user_success
from credentials_service.tests.steps.device_auth_steps import step_device_auth
from credentials_service.tests.steps.device_lang_update_steps import step_device_lang_update
from credentials_service.tests.steps.device_info_steps import step_get_and_check_device_info
from credentials_service.tests.steps.update_user_steps import step_update_user


class CredentialServiceTestCases(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            device_id='string',
            user_id='b58c689d-845b-4503-a77f-6f1b316a52d9',
            language='string'
        )
        self.context.refresh_token = '0eb7ca77-9427-3611-8ecc-bf24f5a7d82b'

    @allure.description('Проверка запроса информации о девайсе')
    def test_get_device_info(self):
        step_get_and_check_device_info(self.context)
        step_device_auth(self.context)
        step_device_lang_update(self.context)


class CreateUserDemo(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            prospect_id="2e625ddf-d6bc-39d0-8a43-209905fa8957",
            phone="string",
            model="string",
            language="ru",
            identity_sign=0,
            device_id="string",
            i_abs_id="string",
            i_abs_code="string"
        )

    @allure.description("Проверка запроса создания пользователя")
    def test_create_user(self):
        create_user_success(self.context)
        step_update_user(self.context)


class UpdateUserDemo(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            prospect_id="2e625ddf-d6bc-39d0-8a43-209905fa8957",
            phone="string",
            model="string",
            language="ru",
            identity_sign=0,
            device_id="string",
            i_abs_id="string",
            i_abs_code="string",
            user_id="b58c689d-845b-4503-a77f-6f1b316a52d9"
        )

    @allure.step("проверка запроса обновления пользователя")
    def test_update_user(self):
        step_update_user(self.context)
