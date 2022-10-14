from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseTypeParent
import allure


class CheckPhoneResponseDatatype(BaseTypeParent):

    def __init__(self, data):
        super().__init__()
        self.data = data

    def check(self, context, **kwargs):
        self.assert_not_empty_str("data")

    @allure.step("Установим данные ответа к контексту")
    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_prospect_id_to_obj(obj)

    def _set_prospect_id_to_obj(self, obj):
        obj.prospect_id = self
