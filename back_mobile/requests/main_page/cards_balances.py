from back_mobile.response_data_types.main_page.balances import Balances
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class CardBalances(TestRequest):
    def __init__(self, client, cards: list = None):
        super().__init__(
            URLProvider().url("back_mobile", "api/v2/mobile/cards-balances"),
            "post",
            data_type=Balances,
            headers=client.auth_token(),
            parameters_in_list=True,
            name_of_list="cards"
        )
        self.cards: list = cards if cards else \
            client.cards.get_card_id_ps_code_from(client.cards.cards)
