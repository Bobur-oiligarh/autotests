from api_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens
from utils.api_utils.test_request import TestRequest
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider


class FinishRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "finish_reg"),
            data_type=AccRefTokens
        )
        self.code = client.code
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.lang_id = client.device.lang_id
        self.sign_id = client.sign_id
