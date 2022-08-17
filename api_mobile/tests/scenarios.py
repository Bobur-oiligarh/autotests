from api_mobile.tests.registration_tests import StartRegistrationSteps, FinishRegistrationTest
from utils.db.models.dbo_signature import DBOSignature
from utils.test_data.client import Client, User, Device

import unittest

import allure


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
        StartRegistrationSteps().startReg(self.client)

        with allure.step("Имитируем получение СМС кода"):
            self.client.code = DBOSignature().sms_key(self.client.sign_id)

        FinishRegistrationTest().finishReg(self.client)


