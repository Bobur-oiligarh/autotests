import allure
from onboarding_physical.response_data_types.hmb.prospect_profile_reponse_data_type import ProspectProfileResponseType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext


class ProspectByClientID(ProspectProfileResponseType):

    def __init__(self, data: dict):
        super().__init__()
        self.rs_client_id = data['RSClientID']
        self.state = data['State']
        self.is_affiliated = data['IsAffiliated']
        self.is_terrorist = data['IsTerrorist']
        self.is_profile_complete = data['IsProfileComplete']
        self.is_consent_needed = data['IsConsentNeeded']
        self.is_actualization_needed = data['IsActualizationNeeded']
        self.verified_at = data['VerifiedAt']
        self.verification_type = data['VerificationType']
        self.verification_id = data['VerificationID']
        self.checked_at = data['CheckedAt']
        self.approved_at = data['ApprovedAt']
        self.approval_sign_id = data['ApprovalSignID']
        self.contacts = data['Contacts']
        self.profiles = data['Profiles']
        self.full_profiles = data['FullProfile']

    def check(self, context, **kwargs):
        self.assert_not_empty_str('pinfl')
        self.assert_not_empty_str('doc_series')
        self.assert_not_empty_str('doc_number')
        self.assert_not_empty_str('birth_date')
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('iabs_id')
        self.assert_not_empty_int('state')
        self.assert_not_empty_bool('is_affiliated')
        self.assert_not_empty_bool('is_terrorist')
        self.assert_not_empty_bool('is_profile_complete')
        self.assert_not_empty_bool('is_actualization_needed')
        self.assert_not_empty_str('verified_at')
        self.assert_not_empty_int('verification_type')
        self.assert_not_empty_str('verification_id')
        self.assert_not_empty_str('created_at')
        self.assert_not_empty_str('updated_at')

    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_prospect_to(obj)

    @allure.step("Установим prospect")
    def _set_prospect_to(self, obj):
        obj.prospect = self

