from back_mobile.response_data_types.references.available_operators import AvailableOperators
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Operators(TestRequest):
    def __init__(self):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/operators"),
            "get",
            data_type=AvailableOperators
        )
