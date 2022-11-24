from credentials_service.response_data_types.device_auth_data_type import DeviceAuthDataType
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class DeviceAuthRequest(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url('credentials_service', 'device-auth'),
            method="post",
            data_type=DeviceAuthDataType
        )
        self.device_id = context.device_id
        self.refresh_token = context.device_info.refresh_token

