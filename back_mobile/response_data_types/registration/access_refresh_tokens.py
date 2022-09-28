import allure

from utils.api_utils.response_data_base import BaseTypeParent
from back_mobile.test_data.client import Client

__all__ = [
    "AccRefTokens",
    "StoreAccRefTokens"
]


class AccRefTokens(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def check(self, context, **kwargs):
        self.assert_not_empty("access_token")
        self.assert_not_empty("refresh_token")

    def set_data_to(self, obj: Client):
        self.set_access_refresh_tokens(obj)

    @allure.step("Установить access_token и refresh_token")
    def set_access_refresh_tokens(self, client):
        self.set_access_token(client)
        self.set_refresh_token(client)

    @allure.step("Установить access_token")
    def set_access_token(self, client):
        client.access_token = self.access_token

    @allure.step("Установить refresh_token")
    def set_refresh_token(self, client):
        client.refresh_token = self.refresh_token


class StoreAccRefTokens(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data["url"]

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        self.assert_not_empty("url")
