from credentials_service.response_data_types.create_user import CreateUser
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostCreateUser(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("credentials_service", "create-user"),
            "post",
            data_type=CreateUser
        )

        self.device_id = context.device_id
        self.identity_sign = context.identity_sign
        self.language = context.language
        self.model = context.model
        self.phone = context.phone
        self.prospect_id = context.prospect_id
