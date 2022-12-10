from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetStrategy(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_credits", f"strategies/{context.strategy.id}"),
            method="get",
            data_type=SMEStrategy,
            require_err_note=False
        )
