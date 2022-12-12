from sme_make_decision_making.response_data_types.lists import SMEList
from sme_make_decision_making.response_data_types.lists import SMELists
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetList(TestRequest):

    def __init__(self, list_id):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", f"list/{list_id}"),
            method="get",
            data_type=SMEList,
            require_err_note=False
        )


class GetLists(TestRequest):

    def __init__(self):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", "list"),
            method="get",
            data_type=SMELists,
            require_err_note=False
        )
