from back_mobile.response_data_types.main_page.cards import Cards
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetClientCards(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-cards"),
            "get",
            data_type=Cards,
            headers=context.auth_token()
        )
