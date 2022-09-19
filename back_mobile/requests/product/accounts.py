from back_mobile.response_data_types.product.accounts_type import OpenedAccounts
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Accounts(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "product", "accounts"),
            data_type=OpenedAccounts,
            headers=client.auth_token()
        )
