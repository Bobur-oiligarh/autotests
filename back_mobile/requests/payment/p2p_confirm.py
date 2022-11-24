from back_mobile.response_data_types.payment.p2p_confirm_result import P2PConfirmResult
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PConfirm(TestRequest):
    def __init__(self, client, confirm_code):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-confirm"),
            "post",
            data_type=P2PConfirmResult,
            headers=client.auth_token()
        )
        self.confirm_code = confirm_code
        self.sign_id = client.sign_id
        self.transact_id = client.p2p_validate_result.transact_id
