from back_mobile.response_data_types.references.exchange_rates_type import ExchangeRateList
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class ExchangeRateRequest(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/exchange-rates"),
            "get",
            data_type=ExchangeRateList,
            headers=client.auth_token(),
        )
