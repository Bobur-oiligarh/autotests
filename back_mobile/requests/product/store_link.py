from back_mobile.response_data_types.product.store_link_type import StoreLinkType
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class StoreLink(TestRequest):
    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/store/1"),
            "get",
            data_type=StoreLinkType,
            headers=client.auth_token()
        )
