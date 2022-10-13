from back_mobile.response_data_types.references.atm import ATMs
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class Bancomates(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/bankomates"),
            "get",
            data_type=ATMs,
            headers=client.auth_token(),
            params={"region_code": client.region_code}
        )
