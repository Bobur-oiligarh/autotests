from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class DeleteList(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", f"list/{context.list.list_id}"),
            method="delete",
            data_type=None,
            require_err_note=False
        )
