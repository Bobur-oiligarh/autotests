from back_mobile.response_data_types.auth.device_identify_sign import DeviceIdentifySign
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostRefreshToken(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/refresh"),
            "post",
            data_type=DeviceIdentifySign
        )
        self.device_id = context.device.device_id
        self.token = context.refresh_token
