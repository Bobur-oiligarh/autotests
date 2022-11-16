from card_service.response_data_types.cards_methods.p2p_info import P2PInfo
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class GetP2PInfo(TestRequest):
    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("card_service", f"v2/p2p-info/{context.card_number}"),
            data_type=P2PInfo,
            method="get"
        )
