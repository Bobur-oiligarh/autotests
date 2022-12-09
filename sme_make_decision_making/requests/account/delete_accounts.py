from sme_make_decision_making.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class DeleteAccounts(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url(service_name="sme_make_decision_making", end_point=f"accounts/{context.account.id}"),
            method="delete",
            data_type=None,
            require_err_note=False
        )
