from credentials_service.response_data_types.device_auth import DeviceAuth
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostDeviceAuth(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url('credentials_service', 'device-auth'),
            method="post",
            data_type=DeviceAuth
        )
        self.device_id = context.device_id
        self.refresh_token = context.device_info.refresh_token

