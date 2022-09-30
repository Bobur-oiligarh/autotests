from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.response_data_base import BaseTypeParent
import allure


class DeviceResponseType(BaseTypeParent):

    def __init__(self, data):
        super().__init__()
        self.user_id = data['user_id']
        self.device_id = data['device_id']
        self.refresh_token = data['refresh_token']
        self.language = data['language']
        self.model = data['model']
        self.identity_sign = data['identity_sign']
        self.active = data['active']

    def check(self, context, **kwargs):
        self.assert_not_empty('user_id')
        self.assert_not_empty('device_id')
        self.assert_not_empty('refresh_token')
        self.assert_not_empty('language')
        self.assert_not_empty('model')
        self.assert_not_empty_int('identity_sign')
        self.assert_not_empty_bool('active')

    def set_data_to(self, obj: CredentialServiceContext):
        self._set_info_to_device(obj)

    @allure.step('Устанавливаем инфо к девайсу')
    def _set_info_to_device(self, obj: CredentialServiceContext):
        obj.device_info = self
