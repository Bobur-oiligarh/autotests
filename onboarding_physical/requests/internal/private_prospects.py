from onboarding_physical.response_data_types.internal.private_prospects_data_type import PrivateProspectDataType
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PrivateProspectsRequest(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("onboarding_physical", "private/prospects"),
            "post",
            data_type=PrivateProspectDataType,
        )
        self.iabs_client_id = context.iabs_id
        self.phone = context.phone
