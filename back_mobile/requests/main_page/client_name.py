from back_mobile.response_data_types.main_page.name import ClientNameType
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientNameRequest(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-name"),
            "get",
            data_type=ClientNameType,
            headers=client.auth_token()
        )
