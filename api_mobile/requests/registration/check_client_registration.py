from api_mobile.response_data_types.registration_data_types import ConfirmMethod
from utils.api_utils.test_request import TestRequest
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider


class CheckClientReg(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "check_client_reg"),
            data_type=ConfirmMethod,
            headers=client.auth_token()
        )
        self.card_number = client.user.card_number
        self.date_expire = client.user.date_expire
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.app_version = client.app_version
