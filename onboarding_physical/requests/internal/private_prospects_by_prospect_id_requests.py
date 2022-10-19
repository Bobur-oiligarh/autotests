from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class PrivateProspectsByID(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/prospects/{context.prospect_id}'),
            data_type=PrivateProspectsByIDResponseDataType,
            params={'load-profile': 'true', 'load-contacts': 'true'}
        )
