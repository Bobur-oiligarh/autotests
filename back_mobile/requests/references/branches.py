from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider
from back_mobile.response_data_types.references.available_branches import AvailableBranches


class Branches(TestRequest):
    """Implements request to branches endpoint."""

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/dict/branches"),
            "get",
            data_type=AvailableBranches,
            headers=client.auth_token(),
            params={'region_code': client.region_code}
        )
