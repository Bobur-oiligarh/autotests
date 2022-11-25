from back_mobile.response_data_types.product.accounts import Accounts
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetAccounts(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/accounts"),
            "get",
            data_type=Accounts,
            headers=context.auth_token()
        )
