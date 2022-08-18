import allure

from api_mobile.response_data_types.registration_data_types import AccRefTokens
from utils.api_utils.test_request import TestRequest
from utils.test_data.client import Client
from utils.test_data.providers import URLProvider


class FinishRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "finish_reg"),
            data_type=AccRefTokens
        )
        self.code = client.code
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.lang_id = client.device.lang_id
        self.sign_id = client.sign_id

    @allure.step("Установить access_token и refresh_token")
    def set_access_refresh_tokens(self, client):
        self.set_access_token(client)
        self.set_refresh_token(client)
        return self

    @allure.step("Установить access_token")
    def set_access_token(self, client):
        client.access_token = self.get_response().data.access_token
        return self

    @allure.step("Установить refresh_token")
    def set_refresh_token(self, client):
        client.refresh_token = self.get_response().data.refresh_token
        return self
