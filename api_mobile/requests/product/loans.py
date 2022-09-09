from api_mobile.response_data_types.product.loans_result import LoansResult
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class Loans(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("product", "loans"),
            data_type=LoansResult,
            headers=client.auth_token()
        )
