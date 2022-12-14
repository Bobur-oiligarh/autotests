from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens
from credentials_service.test_data.credential_service_context import CredentialServiceContext
import allure


class DeviceAuth(AccRefTokens):

    def __init__(self, data: dict):
        super().__init__(data)
        self.identity_sign = data['identity_sign']

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_int('identity_sign')

    def set_data_to(self, obj: CredentialServiceContext):
        self._set_device_auth(obj)

    @allure.step('Устанавливаем аутентифакацию девайсу')
    def _set_device_auth(self, obj):
        obj.device_auth = self

