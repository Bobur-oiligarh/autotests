from back_mobile.response_data_types.payment.p2p_confirm_result import P2PConfirmResult
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PConfirm(TestRequest):
    def __init__(self, client: Client, confirm_code):
        super().__init__(
            URLProvider().url("back_mobile", "payment", "p2p_confirm"),
            data_type=P2PConfirmResult,
            headers=client.auth_token()
        )
        self.confirm_code = confirm_code
        self.sign_id = client.sign_id
        self.transact_id = client.p2p_validate_result.transact_id
