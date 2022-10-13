from back_mobile.response_data_types.product.loans_result import LoansResult
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Loans(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/loans"),
            "get",
            data_type=LoansResult,
            headers=client.auth_token()
        )
