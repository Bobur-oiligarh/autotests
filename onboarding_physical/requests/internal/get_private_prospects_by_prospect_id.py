from onboarding_physical.response_data_types.internal.private_prospects_by_id import \
    PrivateProspectsByID
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetPrivateProspectsByProspectID(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/prospects/{context.prospect_id}'),
            method='get',
            data_type=PrivateProspectsByID,
            params={'load-profile': 'true', 'load-contacts': 'true'}
        )
