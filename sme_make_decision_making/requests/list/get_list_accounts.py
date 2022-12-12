from sme_credits.response_data_types.list.lists import SMEListAccounts
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetListAccounts(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("sme_credits", f"list/{context.list.list_id}/accounts"),
            method="get",
            data_type=SMEListAccounts,
            require_err_note=False
        )
