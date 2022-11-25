from back_mobile.response_data_types.auth.device_identify_sign import DeviceIdentifySign
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostLogin(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/login"),
            "post",
            data_type=DeviceIdentifySign
        )
        self.device_id = context.device.device_id
        self.refresh_token = context.refresh_token
        self.device_os = context.device.device_os
        self.app_version = context.app_version
