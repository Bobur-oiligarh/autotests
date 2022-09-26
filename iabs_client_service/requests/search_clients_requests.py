from iabs_client_service.response_data_types.search_clients_response_data_types import IABSClient
from iabs_client_service.test_data.context import IABSContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class IABSClientByIdRequest(TestRequest):
    """Makes request to get IABS client by his ID."""

    def __init__(self, context: IABSContext):
        super().__init__(
            URLProvider().url("iabs_clients_service", "search_clients", "search_clients_by_id"),
            data_type=IABSClient,
            params={'client_uid': context.iabs_id}
        )
