from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseTypeParent

__all_ = [
    "PrivateProspectDataType"
]


class PrivateProspectDataType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.contact_id = data["contact_id"]
        self.id = data["id"]
        self.state = data["state"]
        self.pinfl = data["pinfl"]
        self.doc_series = data["doc_series"]
        self.doc_number = data["doc_number"]
        self.birth_date = data["birth_date"]
        self.iabs_client_id = data["iabs_client_id"]
        self.iabs_client_code = data["iabs_client_code"]
        self.rs_client_id = data["rs_client_id"]
        self.is_affiliated = data["is_affiliated"]
        self.is_terrorist = data["is_terrorist"]
        self.is_profile_complete = data["is_profile_complete"]
        self.is_consent_needed = data["is_consent_needed"]
        self.is_actualization_needed = data["is_actualization_needed"]
        self.checked_at = data["checked_at"]
        self.approved_at = data["approved_at"]
        self.approval_id = data["approval_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.is_verified = data["is_verified"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("contact_id")
        self.assert_not_empty_str("id")
        self.assert_not_empty_int("state")
        self.assert_not_empty_str("pinfl")
        self.assert_not_empty_str("doc_series")
        self.assert_not_empty_str("doc_number")
        self.assert_not_empty_str("birth_date")
        self.assert_not_empty_str("iabs_client_id")
        self.assert_not_none_and_true_type("iabs_client_code", str)
        self.assert_not_none_and_true_type("rs_client_id", str)
        self.assert_not_empty_bool("is_affiliated")
        self.assert_not_empty_bool("is_terrorist")
        self.assert_not_empty_bool("is_profile_complete")
        self.assert_not_empty_bool("is_actualization_needed")
        self.assert_not_none_and_true_type("approval_id", str)
        self.assert_not_empty_str("created_at")
        self.assert_not_empty_str("updated_at")
        self.assert_not_empty_bool("is_verified")

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    def set_data_to_context(self, context: OnboardingPhysicalContext):
        context.prospect_by_phone_iabs = self
