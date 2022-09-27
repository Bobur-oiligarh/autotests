from tariff_calculator.response_data_types.commision import Commission
from tariff_calculator.test_data.tariff_calculator_context import TariffCalcContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class CalcP2PCommission(TestRequest):

    def __init__(self, context: TariffCalcContext):
        super().__init__(
            URLProvider().url("tariff_calculator", "references", "calc_p2p_comm"),
            data_type=Commission
        )
        self.channel_id = context.channel_id
        self.iabs_id = context.iabs_id
        self.product_id = context.product_id
        self.sum = context.sum
        self.sender = context.sender
        self.receiver = context.receiver
