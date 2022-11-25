from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider
from back_mobile.response_data_types.references.branches import Branches


class GetBranches(TestRequest):
    """Implements request to branches endpoint."""

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/branches"),
            "get",
            data_type=Branches,
            headers=context.auth_token(),
            params={'region_code': context.region_code}
        )
