from unittest import TestCase

import allure

from back_mobile.test_data.client import Client, User, Device
from back_mobile.tests.scenarios.main_page_scenarios import scenario_open_main_page
from back_mobile.tests.scenarios.p2p_scenarios import scenario_card_p2p_transaction
from back_mobile.tests.scenarios.product_scenarios import scenario_products
from back_mobile.tests.scenarios.references_scenarios import scenario_references
from back_mobile.tests.scenarios.registration_scenarios import scenario_registration
from back_mobile.tests.steps.auth_steps import step_login
from back_mobile.tests.steps.main_page_steps import step_client_cards
from back_mobile.tests.steps.settings_steps import step_change_language


class DemoTestCase(TestCase):
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

    @allure.description("Запросы главной страницы")
    def test_main_page(self):
        scenario_registration(self.client)
        scenario_open_main_page(self.client)

    # @allure.description("Перевод по шаблону")
    # def test_template_p2p(self):
    #     scenario_registration(self.client)
    #     step_client_cards(self.client)
    #     scenario_template_p2p_transaction(self.client)

    @allure.description("Перевод по номеру карты")
    def test_card_p2p(self):
        scenario_registration(self.client)
        step_client_cards(self.client)
        scenario_card_p2p_transaction(self.client, "8600120467515865")

    @allure.description("Запросы references")
    def test_references(self):
        scenario_registration(self.client)
        scenario_references(self.client)

    @allure.description("Запросы products")
    def test_products(self):
        scenario_registration(self.client)
        scenario_products(self.client)

    @allure.description("Аутентификация")
    def test_login(self):
        scenario_registration(self.client)
        step_login(self.client)

    @allure.description("Изменение языка")
    def test_change_lang(self):
        scenario_registration(self.client)
        step_change_language(self.client, "uz")
