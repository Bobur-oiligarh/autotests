from back_mobile.response_data_types.product.deposits_result import OpenedDeposits
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Deposits(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "product", "deposits"),
            data_type=OpenedDeposits,
            headers=client.auth_token()
        )
