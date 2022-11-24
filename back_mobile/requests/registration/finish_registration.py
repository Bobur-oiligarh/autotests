from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class FinishRegistration(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/finish-registration"),
            "post",
            data_type=AccRefTokens
        )
        self.code = context.code
        self.device_id = context.device.device_id
        self.device_info = context.device.device_info
        self.lang_id = context.device.lang_id
        self.sign_id = context.sign_id
