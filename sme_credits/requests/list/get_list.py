from sme_credits.response_data_types.list.lists import SMEList
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetList(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("sme_credits", f"list/{context.list.list_id}"),
            method="get",
            data_type=SMEList,
            require_err_note=False
        )
