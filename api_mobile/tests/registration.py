import unittest

from api_mobile.requests.registration import StartRegistration
from utils.test_data.client import Client, User, Device


class RegistrationTest(unittest.TestCase):

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

    def testStartReg(self):
        sr = StartRegistration(self.client)
        response = sr.get_response()
        response.check()
        self.client.sign_id = response.data.sign_id
        print(self.client.sign_id)
