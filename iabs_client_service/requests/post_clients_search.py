from iabs_client_service.response_data_types.search_client_data_type import IABSClient
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostClientsSearch(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url('iabs_client_service', 'clients/search'),
            'post',
            data_type=IABSClient,
            data=context.data
        )
