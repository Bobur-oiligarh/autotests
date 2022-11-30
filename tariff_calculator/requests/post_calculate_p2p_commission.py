from tariff_calculator.response_data_types.commision import Commission
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostCalcP2PCommission(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("tariff_calculator", "calculate-p2p-commission"),
            "post",
            data_type=Commission
        )
        self.channel_id = context.channel_id
        self.iabs_id = context.iabs_id
        self.product_id = context.product_id
        self.sum = context.sum
        self.sender = context.sender
        self.receiver = context.receiver
