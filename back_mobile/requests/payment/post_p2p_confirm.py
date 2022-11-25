from back_mobile.response_data_types.payment.p2p_confirm import P2PConfirm
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostP2PConfirm(TestRequest):
    def __init__(self, context, confirm_code):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-confirm"),
            "post",
            data_type=P2PConfirm,
            headers=context.auth_token()
        )
        self.confirm_code = confirm_code
        self.sign_id = context.sign_id
        self.transact_id = context.p2p_validate_result.transact_id
