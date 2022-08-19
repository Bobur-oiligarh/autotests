import allure
import unittest

from api_mobile.requests.registration.check_client_registration import CheckClientReg
from api_mobile.requests.registration.client_sms_registration import ClientSMSRegistration
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

    @allure.step("Имитируем получение СМС кода (запрос в dbo_signature)")
    def set_SMS_code(self, client):
        client.code = DBOSignature().sms_key(client.sign_id)

    @allure.tag("Процесс регистрации")
    def testScenario(self):
        StartRegistration(self.client) \
            .send_request_check_response(self.client) \
            .response().data.set_sign_id(self.client)

        self.set_SMS_code(self.client)

        FinishRegistration(self.client) \
            .send_request_check_response(self.client) \
            .response().data.set_access_refresh_tokens(self.client)

        GetOffer(self.client) \
            .send_request_check_response(self.client)

        AgreeOffer(self.client) \
            .send_request_check_response(self.client)

        CheckClientReg(self.client) \
            .send_request_check_response(self.client) \
            .response().data.set_sign_id_and_confirm_method(self.client)

        self.set_SMS_code(self.client)

        ClientSMSRegistration(self.client). \
            send_request_check_response(self.client) \
            .response().data.set_access_refresh_tokens(self.client)

        print(self.client.sign_id)
        print(self.client.confirm_method)
