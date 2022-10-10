from unittest import TestCase

import allure

from credentials_service.test_data.credential_service_context import CredentialServiceContext
from credentials_service.tests.steps.create_user_steps import create_user_success
from credentials_service.tests.steps.update_user_steps import step_update_user


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
