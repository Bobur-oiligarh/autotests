from unittest import TestCase

import allure

from api_mobile.test_data.client import Client, User, Device
from card_service.tests.scenarios.info_scenarios import card_info_scenario


class DemoScenarioTestCase(TestCase):
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
        card_info_scenario(self.client)

        with allure.step(f"{self.client.cards}"):
            pass