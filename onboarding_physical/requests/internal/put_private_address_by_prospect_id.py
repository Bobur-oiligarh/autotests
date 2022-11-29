from onboarding_physical.response_data_types.internal.put_private_address_to_prospect import \
    PutPrivateAddressToProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PutPrivateAddress(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/address/{context.prospect_id}'),
            'put',
            data_type=PutPrivateAddressToProspectDataType,
            data=context.private_address
        )
