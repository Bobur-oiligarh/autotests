import allure

from utils.api_utils.response_data_base import BaseTypeParent


class AccRefTokens(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("access_token")
        self.assert_not_empty_str("refresh_token")

    def set_data_to(self, obj):
        self.set_access_refresh_tokens(obj)

    @allure.step("Установить access_token и refresh_token")
    def set_access_refresh_tokens(self, context):
        self.set_access_token(context)
        self.set_refresh_token(context)

    @allure.step("Установить access_token")
    def set_access_token(self, context):
        context.access_token = self.access_token

    @allure.step("Установить refresh_token")
    def set_refresh_token(self, context):
        context.refresh_token = self.refresh_token


class StoreAccRefTokens(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data["url"]

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_str("url")
