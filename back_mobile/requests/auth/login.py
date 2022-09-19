from back_mobile.response_data_types.auth.device_identify_sign import DeviceIdentifySign
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Login(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "auth", "login"),
            data_type=DeviceIdentifySign
        )
        self.device_id = client.device.device_id
        self.refresh_token = client.refresh_token
        self.device_os = client.device.device_os
        self.app_version = client.app_version
