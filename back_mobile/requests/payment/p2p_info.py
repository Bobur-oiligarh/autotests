from back_mobile.response_data_types.payment.card_info import CardInfo
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PInfo(TestRequest):
    def __init__(self, client, card_number: str):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-info/" + card_number),
            "get",
            data_type=CardInfo,
            headers=client.auth_token()
        )
