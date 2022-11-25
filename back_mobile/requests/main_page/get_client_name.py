from back_mobile.response_data_types.main_page.name import ClientName
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class GetClientName(TestRequest):

    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/client-name"),
            "get",
            data_type=ClientName,
            headers=context.auth_token()
        )
