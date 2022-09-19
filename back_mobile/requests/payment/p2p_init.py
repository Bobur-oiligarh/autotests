from back_mobile.response_data_types.registration import SignId
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PInit(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "payment", "p2p_init"),
            data_type=SignId,
            headers=client.auth_token()
        )
        self.action = client.p2p_init_action
        self.transact_id = client.p2p_validate_result.transact_id
