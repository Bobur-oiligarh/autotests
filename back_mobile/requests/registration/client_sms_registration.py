from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientSMSRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "registration", "client_sms_reg"),
            data_type=AccRefTokens,
            headers=client.auth_token()
        )
        self.code = client.code
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.lang_id = client.device.lang_id
        self.sign_id = client.sign_id
