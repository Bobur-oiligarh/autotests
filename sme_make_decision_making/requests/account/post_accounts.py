from sme_make_decision_making.response_data_types.accounts import SMEAccount
from sme_make_decision_making.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostAccounts(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", "accounts"),
            method="post",
            data_type=SMEAccount,
            require_err_note=False
        )
        self.account_mask = context.account.account_mask
        self.active = context.account.active
        self.list_id = context.account.list_id
        self.user_employee = context.account.user_employee

