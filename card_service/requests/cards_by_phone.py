from card_service.response_data_types.infocards import InfoCards
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class CardsByPhone(TestRequest):
    def __init__(self, phone_number):
        super().__init__(
            URLProvider().url("card_service", "info", "cards_by_phone", phone_number),
            data_type=InfoCards,
        )
