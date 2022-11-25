from back_mobile.response_data_types.registration.sign_id import SignId
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostStartReg(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/start-registration"),
            "post",
            data_type=SignId
        )

        self.phone = context.user.phone_number
        self.phone_type = context.device.phone_type
        self.device_id = context.device.device_id
        self.device_info = context.device.device_info
        self.device_os = context.device.device_os
        self.lang_id = context.device.lang_id
        self.app_version = context.app_version
