from api_mobile.response_data_types.product.store_link_type import StoreLinkType
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class StoreLink(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("product", "store_link"),
            data_type=StoreLinkType,
            headers=client.auth_token()
        )
