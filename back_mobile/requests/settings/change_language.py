from back_mobile.response_data_types.settings.language import ChangeLangResult
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ChangeLanguage(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "settings", "change_language"),
            data_type=ChangeLangResult,
            headers=client.auth_token()
        )
        self.device_id = client.device.device_id
        self.lang_id = client.device.lang_id
