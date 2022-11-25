from back_mobile.response_data_types.product.deposits import Deposits
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetDeposits(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/deposits"),
            "get",
            data_type=Deposits,
            headers=context.auth_token()
        )
