from back_mobile.response_data_types.registration.confirm_method import ConfirmMethod
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class CheckClientRegistration(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/check-client-registration"),
            "post",
            data_type=ConfirmMethod,
            headers=client.auth_token()
        )
        self.card_number = client.user.card_number
        self.date_expire = client.user.date_expire
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.app_version = client.app_version
