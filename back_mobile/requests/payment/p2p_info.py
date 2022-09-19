from back_mobile.response_data_types.payment.card_info import CardInfo
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PInfo(TestRequest):
    def __init__(self, client: Client, card_number: str):
        super().__init__(
            URLProvider().url("back_mobile", "payment", "p2p_info", card_number),
            data_type=CardInfo,
            headers=client.auth_token()
        )
