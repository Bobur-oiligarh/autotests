from back_mobile.response_data_types.payment.templates import Templates
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PTemplates(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-templates"),
            "get",
            data_type=Templates,
            headers=client.auth_token()
        )
