from back_mobile.response_data_types.main_page.cards import Cards
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientCards(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "main_page", "client_cards"),
            data_type=Cards,
            headers=client.auth_token()
        )
