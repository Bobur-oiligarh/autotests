from back_mobile.response_data_types.main_page.cards import Cards
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientCards(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-cards"),
            "get",
            data_type=Cards,
            headers=client.auth_token()
        )
