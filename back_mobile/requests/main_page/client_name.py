from back_mobile.response_data_types.main_page.name import ClientNameType
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class ClientNameRequest(TestRequest):

    def __init__(self, client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-name"),
            "get",
            data_type=ClientNameType,
            headers=client.auth_token()
        )
