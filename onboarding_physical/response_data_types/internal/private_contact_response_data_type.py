import allure
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseTypeParent


class PrivateContactDataType(BaseTypeParent):
    def __init__(self, data: dict):
        super().__init__()
        self.id = data['id']
        self.prospect_id = data['prospect_id']
        self.phone = data['value']
        self.phone_type = data['type']
        self.verified_at = data['verified_at']
        self.created_at = data['created_at']

    def check(self, context, **kwargs):
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('prospect_id')
        self.assert_not_empty_str('phone')
        self.assert_not_empty_int('phone_type')
        self.assert_not_empty_str('verified_at')
        self.assert_not_empty_str('created_at')

    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_contact_to(obj)

    @allure.step('')
    def _set_contact_to(self, obj):
        obj.private_contact = self
