from unittest import TestCase

from back_mobile.test_data.client import Client, User, Device
from back_mobile.tests.steps import step_start_reg_unsupported_version, step_start_reg_empty_phone, \
    step_start_reg_empty_phone_type

__all__ = [
    "StartRegTestCase"
]


class StartRegTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client(
            User(
                "998941775859",
                "8600120480409831",
                "0923",
                residence_of_uz=False
            ),
            Device(
                phone_type="1",
                device_id="string7",
                device_info="string7",
                device_os="Android",
                lang_id="ru"
            )
        )

    def test_start_reg_unsupported_version(self):
        step_start_reg_unsupported_version(self.client)

    def test_start_reg_empty_phone(self):
        step_start_reg_empty_phone(self.client)

    def test_start_reg_empty_phone_type(self):
        step_start_reg_empty_phone_type(self.client)
