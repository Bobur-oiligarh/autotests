from api_mobile.response_data_types.references.atm import ATMs
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class Bancomates(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("references", "bancomates"),
            data_type=ATMs,
            headers=client.auth_token(),
            params={"region_code": client.region_code}
        )
