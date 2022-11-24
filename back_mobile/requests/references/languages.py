from back_mobile.response_data_types.references.available_languages import AvailableLanguages
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Languages(TestRequest):

    def __init__(self):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/languages"),
            "get",
            data_type=AvailableLanguages
        )
