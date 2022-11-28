from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostDeviceLangUpdate(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("credentials_service", "device-language-update"),
            "post",
            data_type=None
        )
        self.device_id = context.device_id
        self.language = context.language
        self.user_id = context.user_id


