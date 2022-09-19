from back_mobile.response_data_types.references.available_languages import AvailableLanguages
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Languages(TestRequest):

    def __init__(self):
        super().__init__(
            URLProvider().url("back_mobile", "references", "languages"),
            data_type=AvailableLanguages
        )
