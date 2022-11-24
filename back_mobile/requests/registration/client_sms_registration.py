from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientSMSRegistration(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-registration"),
            "post",
            data_type=AccRefTokens,
            headers=client.auth_token()
        )
        self.code = client.code
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.lang_id = client.device.lang_id
        self.sign_id = client.sign_id
