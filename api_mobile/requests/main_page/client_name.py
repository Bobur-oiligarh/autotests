from api_mobile.response_data_types.main_page.name import ClientNameType
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientNameRequest(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("main_page", "client_name"),
            data_type=ClientNameType,
            headers=client.auth_token()
        )
