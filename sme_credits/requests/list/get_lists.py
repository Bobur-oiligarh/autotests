from sme_credits.response_data_types.list.lists import SMELists
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetLists(TestRequest):
    def __init__(self):
        super().__init__(
            url=URLProvider().url("sme_credits", "list"),
            method="get",
            data_type=SMELists,
            require_err_note=False
        )
