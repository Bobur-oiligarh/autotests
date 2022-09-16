from api_mobile.response_data_types.registration.confirm_method import ConfirmMethod
from utils.api_utils.test_request import TestRequest
from api_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider


class CheckClientRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "registration", "check_client_reg"),
            data_type=ConfirmMethod,
            headers=client.auth_token()
        )
        self.card_number = client.user.card_number
        self.date_expire = client.user.date_expire
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.app_version = client.app_version
