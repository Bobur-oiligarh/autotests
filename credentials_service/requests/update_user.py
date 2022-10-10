from credentials_service.response_data_types import CreateUserDataType
from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider

__all__ = [
    "UpdateUser"
]


class UpdateUser(TestRequest):
    def __init__(self, context: CredentialServiceContext):
        super().__init__(
            URLProvider().url("credentials_service", "references", "update_user"),
            data_type=CreateUserDataType
        )
        self.device_id = context.device_id
        self.i_abs_code = context.i_abs_code
        self.i_abs_id = context.i_abs_id
        self.identity_sign = context.identity_sign
        self.phone = context.phone
        self.prospect_id = context.prospect_id
        self.user_id = context.user_id
