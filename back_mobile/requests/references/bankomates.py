from back_mobile.response_data_types.references.atm import ATMs
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Bancomates(TestRequest):
    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/bankomates"),
            "get",
            data_type=ATMs,
            headers=client.auth_token(),
            params={"region_code": client.region_code}
        )
