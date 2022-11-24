from limit_module.response_data_types.p2p_all_oper_limit_data_types import LimitDataTypes
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class P2PAllOperationsLimitRequest(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("limit_module", "p2p-all"),
            "post",
            data_type=LimitDataTypes
        )
        self.product_id = context.product_id
        self.iabs_id = context.iabs_id
        self.limit_types = context.limit_types


