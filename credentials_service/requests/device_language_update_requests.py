from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class DeviceLangUpdateRequest(TestRequest):

    def __init__(self, context: CredentialServiceContext):
        super().__init__(
            URLProvider().url("credentials_service", "references", "device_language_update"),
            data_type=None
        )
        self.device_id = context.device_id
        self.language = context.language
        self.user_id = context.user_id


