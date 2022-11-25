from back_mobile.response_data_types.registration.confirm_method import ConfirmMethod
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostCheckClientReg(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/check-client-registration"),
            "post",
            data_type=ConfirmMethod,
            headers=context.auth_token()
        )
        self.card_number = context.user.card_number
        self.date_expire = context.user.date_expire
        self.device_info = context.device.device_info
        self.device_os = context.device.device_os
        self.app_version = context.app_version
