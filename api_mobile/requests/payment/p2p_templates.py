from api_mobile.response_data_types.payment.templates import Templates
from api_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PTemplates(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "payment", "p2p_templates"),
            data_type=Templates,
            headers=client.auth_token()
        )
