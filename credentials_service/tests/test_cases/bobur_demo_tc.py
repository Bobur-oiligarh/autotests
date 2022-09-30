from unittest import TestCase

from credentials_service.test_data.credential_service_context import CredentialServiceContext
from credentials_service.tests.steps.get_device_info_steps import step_get_and_check_device_info


class CredentialServiceTestCases(TestCase):

    def setUp(self) -> None:
        self.context = CredentialServiceContext(
            device_id='string',
            user_id='b58c689d-845b-4503-a77f-6f1b316a52d9'
        )

    def test_get_device_info(self):
        step_get_and_check_device_info(self.context)
