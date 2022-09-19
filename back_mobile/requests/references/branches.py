from back_mobile.test_data.client import Client
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider
from back_mobile.response_data_types.references.available_branches import AvailableBranches


class Branches(TestRequest):
    """Implements request to branches endpoint."""

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "references", "branches"),
            data_type=AvailableBranches,
            headers=client.auth_token(),
            params={'region_code': client.region_code}
        )
