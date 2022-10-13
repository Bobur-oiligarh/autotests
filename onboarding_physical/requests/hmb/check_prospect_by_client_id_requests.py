from onboarding_physical.response_data_types.hmb.prospect_by_clientID_data_types import ProspectByClientID
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class CheckProspectByClientID(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', 'check-prospect-by-client-id'),
            "post",
            data_type=ProspectByClientID
        )
        self.iabs_id = context.iabs_id
