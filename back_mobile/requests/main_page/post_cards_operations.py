from back_mobile.response_data_types.main_page.operations import Operations
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostCardsOperations(TestRequest):

    def __init__(self, context, cards: list = None):
        super().__init__(
            URLProvider().url("back_mobile", "api/v2/mobile/cards-operations"),
            "post",
            data_type=Operations,
            headers=context.auth_token()
        )
        self.cards = cards if cards else context.cards.get_card_id_ps_code_from(context.cards.cards, False)
