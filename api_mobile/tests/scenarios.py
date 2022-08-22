import allure
import unittest

from api_mobile.requests.registration import StartRegistration, FinishRegistration, GetOffer, AgreeOffer, \
    CheckClientRegistration, ClientSMSRegistration
from api_mobile.test_data.db_models.dbo_signature import DBOSignature
from api_mobile.test_data.client import Client, User, Device
from utils.universal_steps.check_response import check_response_status


@allure.story("Registration scenario, positive")
class RegistrationScenarioTest(unittest.TestCase):

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

    @allure.step("Имитируем получение СМС кода (запрос в dbo_signature)")
    def set_SMS_code(self, client):
        client.code = DBOSignature().sms_key(client.sign_id)

    @allure.testcase("Процесс регистрации")
    def testScenario(self):
        self.step_start_reg()
        self.set_SMS_code(self.client)
        self.step_finish_reg()
        self.step_get_offer()
        self.step_agree_offer()
        self.step_check_client_reg()
        self.set_SMS_code(self.client)
        self.step_client_sms_reg()

    @allure.step("Начало регистрации start_registration")
    def step_start_reg(self):
        response = StartRegistration(self.client).response()
        check_response_status(response)
        response.data.set_sign_id(self.client)

    @allure.step("Подтверждение номера телефона finish_registration")
    def step_finish_reg(self):
        response = FinishRegistration(self.client).response()
        check_response_status(response)
        response.data.set_access_refresh_tokens(self.client)

    @allure.step("Запрос оферты get_offer")
    def step_get_offer(self):
        response = GetOffer(self.client).response()
        check_response_status(response)

    @allure.step("Подтверждение оферты agree_offer")
    def step_agree_offer(self):
        response = AgreeOffer(self.client).response()
        check_response_status(response)

    @allure.step("Добавление карты check_client_registration")
    def step_check_client_reg(self):
        response = CheckClientRegistration(self.client).response()
        check_response_status(response)
        response.data.set_sign_id_and_confirm_method(self.client)

    @allure.step("Подтверждение номера карты через СМС client_sms_registration")
    def step_client_sms_reg(self):
        response = ClientSMSRegistration(self.client).response()
        check_response_status(response)
        response.data.set_access_refresh_tokens(self.client)
