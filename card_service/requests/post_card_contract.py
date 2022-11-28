from card_service.response_data_types.card_contract import CardContract
from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostCardContract(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("card_service", "card/contract/"),
            "post",
            data_type=CardContract
        )
        self.card_number = context.card_number
