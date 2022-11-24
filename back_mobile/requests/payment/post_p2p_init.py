from back_mobile.response_data_types.registration.sign_id import SignId
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostP2PInit(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-init"),
            "post",
            data_type=SignId,
            headers=context.auth_token()
        )
        self.action = context.p2p_init_action
        self.transact_id = context.p2p_validate_result.transact_id
