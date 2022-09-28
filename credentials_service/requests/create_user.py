from credentials_service.response_data_types.create_user_data_type import CreateUserDataType
from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider

__all__ = [
    "CreateUser"
]


class CreateUser(TestRequest):
    def __init__(self, context: CredentialServiceContext):
        super().__init__(
            URLProvider().url("credentials_service", "references", "create_user"),
            data_type=CreateUserDataType
        )

        self.device_id = context.device_id
        self.identity_sign = context.identity_sign
        self.language = context.language
        self.model = context.model
        self.phone = context.phone
        self.prospect_id = context.prospect_id
