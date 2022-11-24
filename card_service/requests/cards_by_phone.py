from card_service.response_data_types import InfoCards
from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class CardsByPhone(TestRequest):
    def __init__(self, context: CardServiceContext):
        super().__init__(
            URLProvider().url("card_service", "card/bank-cards/by-phone/" + context.phone_number),
            "get",
            data_type=InfoCards,
        )
