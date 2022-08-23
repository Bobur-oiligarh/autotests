from unittest import TestCase

from api_mobile.test_data.client import Client, User, Device
from api_mobile.tests.scenarios.registration import scenario_registration


class RegistrationScenarioTestCase(TestCase):
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

    def test_registration(self):
        scenario_registration(self.client)
