from sme_credits.response_data_types.accounts_data_type import SMEAccount
from sme_credits.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class PatchAccounts(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url("sme_credits", f"accounts/{context.id}"),
            method="post",
            data_type=SMEAccount,
            require_err_note=False
        )
        self.account_mask = context.account_mask
        self.active = context.active
        self.list_id = context.list_id

        print(super()._url)
