from api_mobile.response_data_types.references.available_languages import AvailableLanguages
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class Languages(TestRequest):

    def __init__(self):
        super().__init__(
            URLProvider().url("references", "languages"),
            data_type=AvailableLanguages
        )
