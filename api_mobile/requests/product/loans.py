from api_mobile.response_data_types.product.loans_result import LoansResult
from api_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Loans(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "product", "loans"),
            data_type=LoansResult,
            headers=client.auth_token()
        )
