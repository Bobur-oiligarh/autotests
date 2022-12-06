from sme_credits.response_data_types.strategy.strategies import SMEStrategy
from sme_credits.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostStrategy(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_credits", "strategies"),
            method="post",
            data_type=SMEStrategy,
            require_err_note=False
        )
        self.product_id = context.strategy.product_id
        self.step_id = context.strategy.step_id
        self.user_employee = context.strategy.user_employee
        self.active = context.strategy.active



