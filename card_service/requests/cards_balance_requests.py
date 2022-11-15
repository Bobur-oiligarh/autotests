from card_service.response_data_types.cards_balance_data_type import CardsBalance
from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class CardsBalanceRequest(TestRequest):

    def __init__(self, cards_context: CardServiceContext):
        super().__init__(
            URLProvider().url("back_mobile", "v2/balances"),
            "get",
            data_type=CardsBalance
        )
        self.cards_id = [card["card_id"] for card in cards_context.cards]
