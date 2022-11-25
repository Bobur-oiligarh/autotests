from back_mobile.response_data_types.references.exchange_rates import ExchangeRates
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetExchangeRates(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/exchange-rates"),
            "get",
            data_type=ExchangeRates,
            headers=context.auth_token(),
        )
