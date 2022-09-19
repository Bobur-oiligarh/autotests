from back_mobile.response_data_types.product.store_link_type import StoreLinkType
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class StoreLink(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "product", "store_link"),
            data_type=StoreLinkType,
            headers=client.auth_token()
        )
