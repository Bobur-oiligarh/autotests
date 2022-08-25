from api_mobile.response_data_types.main_page.cards import Cards
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientCards(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("main_page", "client_cards"),
            data_type=Cards,
            headers=client.auth_token()
        )
