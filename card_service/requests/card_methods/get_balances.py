from card_service.response_data_types.cards_methods.balances import CardsBalance
from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class GetBalancesRequest(TestRequest):
    def __init__(self, cards_context: CardServiceContext):
        super().__init__(
            URLProvider().url("card_service", "v2/balances"),
            "get",
            data_type=CardsBalance,
            params={"cards_id": [card.card_id for card in cards_context.cards.cards]}
        )
