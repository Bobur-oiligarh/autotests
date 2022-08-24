from api_mobile.response_data_types.main_page.balances import Balances
from api_mobile.response_data_types.main_page.cards import Cards
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class CardBalances(TestRequest):
    def __init__(self, client: Client, cards: list):
        super().__init__(
            URLProvider().url("main_page", "cards_balances"),
            data_type=Balances,
            headers=client.auth_token()
        )
        self.cards: list
        self._set_cards(client.cards)

    def _set_cards(self, cards: Cards):
        pass


