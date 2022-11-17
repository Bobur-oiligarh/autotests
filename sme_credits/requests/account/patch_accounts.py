from sme_credits.response_data_types.accounts_data_type import SMEAccount
from sme_credits.test_data.sme_context import SMEContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class PatchAccounts(TestRequest):
    def __init__(self, context: SMEContext):
        super().__init__(
            url=URLProvider().url(service_name="sme_credits", end_point=f"accounts/{context.account.id}"),
            method="patch",
            data_type=None,
            require_err_note=False
        )
        self.account_mask = context.account.account_mask
        self.list_id = context.account.list_id
        self.active = context.account.active



