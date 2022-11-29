from onboarding_physical.response_data_types.internal.private_prospects import PrivateProspect
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostPrivateProspects(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("onboarding_physical", "private/prospects"),
            "post",
            data_type=PrivateProspect,
        )
        self.iabs_client_id = context.iabs_id
        self.phone = context.phone
