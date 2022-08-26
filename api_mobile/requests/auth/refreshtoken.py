from api_mobile.response_data_types.auth.device_identify_sign import DeviceIdentifySign
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class RefreshToken(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("auth", "refreshtoken"),
            data_type=DeviceIdentifySign
        )
        self.device_id = client.device.device_id
        self.token = client.refresh_token
