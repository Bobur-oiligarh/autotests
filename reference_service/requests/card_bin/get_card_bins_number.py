from reference_service.response_data_types.card_bin import CardBinNumber
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetCardBinsNumber(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("reference_service", "card-bins/number/" + context.card_number),
            "get",
            data_type=CardBinNumber
        )
