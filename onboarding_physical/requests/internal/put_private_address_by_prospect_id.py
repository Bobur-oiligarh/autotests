from onboarding_physical.response_data_types.internal.put_private_address_to_prospect_data_type import \
    PutPrivateAddressToProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider
import allure


class PutPrivateAddressRequest(TestRequest):

    def __init__(self, context: OnboardingPhysicalContext):
        super().__init__(
            URLProvider().url('onboarding_physical', f'private/address/{context.prospect_id}'),
            'put',
            data_type=PutPrivateAddressToProspectDataType,
            data={
                'id': '2056e105-703e-4d60-9af7-055ee56bbf56',
                'profile_id': '964b1484-00d4-4c22-b893-687743ded710',
                'address': 'ТОШКЕНТ ШАҲРИ; ЯШНОБОД ТУМАНИ; г. Ташкент, Яшнабадский район, ул. Авиасозлар, пр. 1, '
                           'Алимкент МСГ, 4- Дом, 10- Квартира',
                'registered_at': '2021-05-04T00:00:00Z',
                'country_code': '860',
                'region_code': '26',
                'district_code': '207',
                'kadastr': '10:04:04:03:01:5005:0001:010',
                'created_at': '2022-04-25T04:01:44.207872Z'
            }
        )
