import allure

from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseTypeParent


# class PrivateContacts(BaseTypeParent):
#
#     def __init__(self, data: dict):
#         super().__init__()
#         self.contacts: list = self.deserialize_to_list_of(PrivateContactDataType, data)
#
#     def check(self, context: OnboardingPhysicalContext, **kwargs):
#         self.check_list_of(list_param_name="contacts", context=context, **kwargs)
#
#     def set_data_to(self, obj: OnboardingPhysicalContext):
#         self._set_contacts(obj)
#
#     @allure.step("Установим контакты")
#     def _set_contacts(self, obj):
#         obj.private_contacts = self
