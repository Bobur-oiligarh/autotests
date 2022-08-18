import allure
import unittest

from api_mobile.requests.registration.finish_registration import FinishRegistration
from api_mobile.requests.registration.offer import GetOffer, AgreeOffer
from api_mobile.requests.registration.start_registration import StartRegistration
from api_mobile.test_data.db_models.dbo_signature import DBOSignature
from api_mobile.test_data.client import Client, User, Device


@allure.story("Registration scenario, positive")
class RegistrationScenarioTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client(
            User(
                "998935087121",
                "8600120436901998",
                "1023"
            ),
            Device(
                phone_type="1",
                device_id="string7",
                device_info="string7",
                device_os="Android",
                lang_id="ru"
            )
        )

    def testScenario(self):
        StartRegistration(self.client) \
            .check_response(self.client) \
            .set_sign_id(self.client)

        with allure.step("Имитируем получение СМС кода (запрос из БД)"):
            self.client.code = DBOSignature().sms_key(self.client.sign_id)

        FinishRegistration(self.client) \
            .check_response(self.client) \
            .set_access_refresh_tokens(self.client)

        GetOffer(self.client) \
            .check_response(self.client)

        AgreeOffer(self.client) \
            .check_response(self.client)
