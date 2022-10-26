from iabs_client_service.response_data_types.search_client_data_type import IABSClientDataType
from iabs_client_service.test_data.context import IABSContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class IABSClientByIdRequest(TestRequest):

    def __init__(self, context: IABSContext):
        super().__init__(
            URLProvider().url("iabs_client_service", "clients/search"),
            "get",
            data_type=IABSClientDataType,
            params={'client_uid': context.iabs_id}
        )
