import allure

from api_mobile.response_data_types.response_data_base import BaseType


class AccRefTokens(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def check(self, client, **kwargs):
        self.access_token_not_empty()
        self.refresh_token_not_empty()

    @allure.step("access_token не пустой")
    def access_token_not_empty(self):
        self.tc.assertNotEqual(self.access_token, "", f"access_token ответа пустой" + self.__str__())

    @allure.step("refresh_token не пустой")
    def refresh_token_not_empty(self):
        self.tc.assertNotEqual(self.refresh_token, "", f"refresh_token ответа пустой" + self.__str__())

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

    def url_not_empty(self):
        self.tc.assertNotEqual(self.url, "", f"url в ответе пустой" + self.__str__())
