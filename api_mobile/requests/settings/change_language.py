from api_mobile.response_data_types.settings.language import ChangeLangResult
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class ChangeLanguage(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("settings", "change_language"),
            data_type=ChangeLangResult,
            headers=client.auth_token()
        )
        self.device_id = client.device.device_id
        self.lang_id = client.device.lang_id
