from reference_service.response_data_types.card_bin import CardBinNumberResult
from reference_service.test_data.reference_context import ReferenceServiceContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class CardBinsNumber(TestRequest):
    def __init__(self, context: ReferenceServiceContext):
        super().__init__(
            URLProvider().url("reference_service", "card-bins/number/" + context.card_number),
            "get",
            data_type=CardBinNumberResult
        )
