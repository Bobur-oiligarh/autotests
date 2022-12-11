from sme_make_decision_making.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PatchStrategy(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", f"strategies/{context.strategy.id}"),
            method="patch",
            data_type=None,
            require_err_note=False
        )
        self.product_id = context.strategy.product_id
        self.active = context.strategy.active
