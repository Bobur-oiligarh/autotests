from unittest import TestCase

import allure

from credentials_service.test_data.credential_service_context import CredentialServiceContext
from credentials_service.tests.steps.create_user_steps import create_user_success


class CredentialServiceDemo(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            prospect_id="2e625ddf-d6bc-39d0-8a43-209905fa8957",
            phone="string",
            model="string",
            language="ru",
            identity_sign=0,
            device_id="string"
        )

    @allure.description("Проверка запроса создания пользователя")
    def test_create_user(self):
        create_user_success(self.context)
