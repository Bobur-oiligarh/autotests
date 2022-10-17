import allure
from onboarding_physical.response_data_types.internal.private_prospects_data_type import PrivateProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext


class PrivateContactDataType(PrivateProspectDataType):
    def __init__(self, data: dict):
        super().__init__(data=data)
        self.phone_type = data['type']
        self.phone = data['value']


    def check(self, context, **kwargs):
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('prospect_id')
        self.assert_not_empty_str('value')
        self.assert_not_empty_int('phone_type')
        self.assert_not_empty_str('verified_at')
        self.assert_not_empty_str('created_at')

    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_contact_to(obj)

    @allure.step('')
    def _set_contact_to(self, obj):
        obj.private_contact = self

