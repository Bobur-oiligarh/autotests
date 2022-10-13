from back_mobile.response_data_types.references.exchange_rates_type import ExchangeRateList
from back_mobile.test_data.client import Client
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class ExchangeRateRequest(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/exchange-rates"),
            "get",
            data_type=ExchangeRateList,
            headers=client.auth_token(),
        )
