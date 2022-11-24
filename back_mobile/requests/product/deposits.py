from back_mobile.response_data_types.product.deposits_result import OpenedDeposits
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Deposits(TestRequest):
    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/deposits"),
            "get",
            data_type=OpenedDeposits,
            headers=client.auth_token()
        )
