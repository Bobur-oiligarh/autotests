from limit_module.response_data_types.p2p_all_oper_limit import Limits
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostP2PAllOperationsLimit(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("limit_module", "operation/p2p-all"),
            method="post",
            data_type=Limits
        )
        self.product_id = context.product_id
        self.iabs_id = context.iabs_id
        self.limit_types = context.limit_types


