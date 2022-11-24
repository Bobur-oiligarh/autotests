from onboarding_physical.response_data_types.internal.private_contact_response_data_type import PrivateContactDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PrivateContactRequest(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', 'private/contact'),
            method='post',
            data_type=PrivateContactDataType
        )
        self.phone = context.phone
        self.prospect_id = context.prospect_id
        self.type = context.contact_type
