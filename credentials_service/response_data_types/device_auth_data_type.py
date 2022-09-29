from credentials_service.test_data.credential_service_context import CredentialServiceContext
from utils.api_utils.response_data_base import BaseTypeParent
import allure


class DeviceAuthDataType(BaseTypeParent):

    def __init__(self, data):
        super().__init__()
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        self.identity_sign = data['identity_sign']

    def check(self, context, **kwargs):
        self.assert_not_empty('access_token')
        self.assert_not_empty('refresh_token')
        self.assert_not_empty('identity_sign')

    def set_data_to(self, obj: CredentialServiceContext):
        self._set_device_auth(obj)

    @allure.step('Устанавливаем аутентифакацию девайсу')
    def _set_device_auth(self, obj):
        obj.device_auth = self

