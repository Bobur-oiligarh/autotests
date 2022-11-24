from back_mobile.response_data_types.product.loans import Loans
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetLoans(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/loans"),
            "get",
            data_type=Loans,
            headers=context.auth_token()
        )
