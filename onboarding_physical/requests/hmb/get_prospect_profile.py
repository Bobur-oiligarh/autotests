from onboarding_physical.response_data_types.hmb.prospect_profile import ProspectProfile
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetProspectProfile(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', 'get-prospect-profile'),
            "get",
            data_type=ProspectProfile,
            params={'prospectID': context.prospect_id}
        )
