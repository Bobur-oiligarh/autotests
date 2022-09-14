from api_mobile.response_data_types.product.deposits_result import OpenedDeposits
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class Deposits(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("product", "deposits"),
            data_type=OpenedDeposits,
            headers=client.auth_token()
        )
