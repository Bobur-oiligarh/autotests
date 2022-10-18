from onboarding_physical.response_data_types.internal.private_contacts_response_data_type import PrivateContacts
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class PrivateContactsRequest(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/contacts/{context.contact_id}'),
            'get',
            data_type=PrivateContactDataType,
        )
