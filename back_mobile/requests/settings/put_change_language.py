from back_mobile.response_data_types.settings.language import ChangeLang
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PutChangeLanguage(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/settings/language"),
            "put",
            data_type=ChangeLang,
            headers=context.auth_token()
        )
        self.device_id = context.device.device_id
        self.lang_id = context.device.lang_id
