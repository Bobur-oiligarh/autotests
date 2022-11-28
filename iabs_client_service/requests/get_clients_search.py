from iabs_client_service.response_data_types.search_client_data_type import IABSClient
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetIABSClientById(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("iabs_client_service", "clients/search"),
            "get",
            data_type=IABSClient,
            params={'client_uid': context.iabs_id}
        )
