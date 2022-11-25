from back_mobile.response_data_types.product.store_link import StoreLink
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetStoreLink(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/product/store/1"),
            "get",
            data_type=StoreLink,
            headers=context.auth_token()
        )
