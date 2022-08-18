import allure

from api_mobile.response_data_types.registration_data_types import SignId
from utils.api_utils.test_request import TestRequest
from utils.test_data.client import Client
from utils.test_data.providers import URLProvider


class StartRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "start_reg"),
            data_type=SignId
        )

        self.phone = client.user.phone_number
        self.phone_type = client.device.phone_type
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.lang_id = client.device.lang_id
        self.app_version = client.app_version

    @allure.step("Установить sign_id")
    def set_sign_id(self, client):
        client.sign_id = self.get_response().data.sign_id
        return self
