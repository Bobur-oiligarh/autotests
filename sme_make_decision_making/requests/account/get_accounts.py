from sme_make_decision_making.response_data_types.accounts import SMEAccounts
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetAccounts(TestRequest):
    def __init__(self):
        super().__init__(
            url=URLProvider().url(service_name="sme_make_decision_making", end_point="accounts"),
            method="get",
            data_type=SMEAccounts,
            require_err_note=False
        )
