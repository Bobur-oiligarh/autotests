from back_mobile.response_data_types.references.atm import ATMs
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetATMs(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/bankomates"),
            "get",
            data_type=ATMs,
            headers=context.auth_token(),
            params={"region_code": context.region_code}
        )
