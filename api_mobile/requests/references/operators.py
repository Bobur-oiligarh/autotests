from api_mobile.response_data_types.references.available_operators import AvailableOperators
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class Operators(TestRequest):
    def __init__(self):
        super().__init__(
            URLProvider().url("references", "operators"),
            data_type=AvailableOperators
        )
