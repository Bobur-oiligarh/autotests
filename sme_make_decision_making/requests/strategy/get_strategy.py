from sme_make_decision_making.response_data_types.strategies import SMEStrategy
from sme_make_decision_making.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetStrategy(TestRequest):
    def __init__(self, strategy_id):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", f"strategies/{strategy_id}"),
            method="get",
            data_type=SMEStrategy,
            require_err_note=False
        )
