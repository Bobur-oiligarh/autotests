from unittest import TestCase

from api_mobile.test_data.client import Client, User, Device
from api_mobile.tests.scenarios.main_page_scenarios import scenario_open_main_page
from api_mobile.tests.scenarios.registration_scenarios import scenario_registration
from api_mobile.tests.steps.auth_steps import step_refresh_token, step_login
from api_mobile.tests.steps.settings_steps import step_change_language


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
        scenario_registration(self.client)
        scenario_open_main_page(self.client)
        step_refresh_token(self.client)
        step_login(self.client)
        step_change_language(self.client, "uz")
        step_change_language(self.client, "ru")


