from unittest import TestCase

import allure

from back_mobile.test_data.client import Client, User, Device
from back_mobile.tests.scenarios.references_scenarios import scenario_references
from back_mobile.tests.scenarios.registration_scenarios import scenario_registration

__all__ = [
    "DemoMainPageTestCase"
]


class DemoMainPageTestCase(TestCase):
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
        self.client.confirm_method = "SMS"

    def test_main_page(self):
        scenario_registration(self.client)
        scenario_references(self.client)
        with allure.step(f"Проверка {self.client.exchange_rates}"):
            pass
