from api_mobile.response_data_types.references.exchange_rates_type import ExchangeRateList
from api_mobile.test_data.client import Client
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class ExchangeRateRequest(TestRequest):
    """Implements request to get exchange rates."""

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("api_mobile", "references", "exchange-rates"),
            data_type=ExchangeRateList,
            headers=client.auth_token(),
        )
