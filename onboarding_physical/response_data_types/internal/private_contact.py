import allure
from utils.api_utils.response_data_base import BaseTypeParent


class PrivateContact(BaseTypeParent):
    def __init__(self, data: dict):
        super().__init__()
        self.id = data.get('id')
        self.prospect_id = data.get('prospect_id')
        self.phone = data.get('value')
        self.phone_type = data.get('type')
        self.verified_at = data.get('verified_at')
        self.created_at = data.get('created_at')

    def check(self, context, **kwargs):
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('prospect_id')
        self.assert_not_empty_str('phone')
        self.assert_not_empty_int('phone_type')
        self.assert_no_strict_str('verified_at')
        self.assert_not_empty_str('created_at')

    def set_data_to(self, obj):
        self._set_contact_to(obj)

    @allure.step('')
    def _set_contact_to(self, obj):
        obj.private_contact = self
