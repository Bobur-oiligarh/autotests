from onboarding_physical.response_data_types.internal.put_private_address_to_prospect_data_type import \
    PutPrivateAddressToProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class PutPrivateAddressRequest(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/address/{context.prospect_id}'),
            'put',
            data_type=PutPrivateAddressToProspectDataType,
            data=context.private_address.__dict__
        )

