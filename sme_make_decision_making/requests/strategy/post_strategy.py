from sme_make_decision_making.response_data_types.strategies import SMEStrategy
from sme_make_decision_making.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostStrategy(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", "strategies"),
            method="post",
            data_type=SMEStrategy,
            require_err_note=False
        )
        self.product_id = context.strategy.product_id
        self.step_id = context.strategy.step_id
        self.user_employee = context.strategy.user_employee
        self.active = context.strategy.active
