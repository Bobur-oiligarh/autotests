from credentials_service.response_data_types.device_info_response_types import DeviceResponseType
from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetDeviceInfo(TestRequest):

    def __init__(self, context: CredentialServiceContext):
        super().__init__(
            URLProvider().url('credentials_service', 'get-device-info'),
            data_type=DeviceResponseType
        )
        self.device_id = context.device_id
        self.user_id = context.user_id