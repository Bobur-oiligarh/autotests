from back_mobile.response_data_types.main_page.operations import Operations
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class CardsOperations(TestRequest):

    def __init__(self, client: Client, cards: list = None):
        super().__init__(
            URLProvider().url("back_mobile", "api/v2/mobile/cards-operations"),
            "post",
            data_type=Operations,
            headers=client.auth_token()
        )
        self.cards = cards if cards else client.cards.get_card_id_ps_code_from(client.cards.cards, False)
