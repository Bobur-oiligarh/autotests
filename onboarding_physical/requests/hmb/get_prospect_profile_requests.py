from onboarding_physical.response_data_types.hmb.prospect_profile_reponse_data_type import ProspectProfileResponseType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class ProspectProfileRequest(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', 'get-prospect-profile'),
            "get",
            data_type=ProspectProfileResponseType,
            params={'prospectID': context.prospect_id}
        )
