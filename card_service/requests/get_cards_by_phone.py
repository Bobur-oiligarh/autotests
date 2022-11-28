from card_service.response_data_types import InfoCards
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetCardsByPhone(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("card_service", "card/bank-cards/by-phone/" + context.phone),
            "get",
            data_type=InfoCards,
        )
