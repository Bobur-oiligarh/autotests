from iabs_client_service.response_data_types import IABSClientDataType
from iabs_client_service.test_data import IABSContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostClientsSearchRequest(TestRequest):

    def __init__(self, context: IABSContext):
        super().__init__(
            URLProvider().url('iabs_client_service', 'clients/search'),
            'post',
            data_type=IABSClientDataType,
            data=context.data
        )
