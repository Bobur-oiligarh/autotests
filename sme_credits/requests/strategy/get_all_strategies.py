from sme_credits.response_data_types.strategy.strategies import SMEStrategies
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetStrategies(TestRequest):
    def __init__(self):
        super().__init__(
            url=URLProvider().url("sme_credits", "strategies"),
            method="get",
            data_type=SMEStrategies,
            require_err_note=False
        )



