from back_mobile.response_data_types.product.accounts_type import OpenedAccounts
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Accounts(TestRequest):
    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/accounts"),
            "get",
            data_type=OpenedAccounts,
            headers=client.auth_token()
        )
