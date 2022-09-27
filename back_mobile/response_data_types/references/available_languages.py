from typing import Any
import allure
from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = [
    "AvailableLanguages",
    "Language"
]


class AvailableLanguages(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.lang_list: list = self.deserialize_to_list_of(Language, data)

    def set_data_to(self, obj):
        self.set_langs(obj)

    @allure.step("Установить доступные языки клиенту")
    def set_langs(self, client):
        client.lang_list = self

    def check(self, client, **kwargs):
        self.check_list_of("lang_list", client, **kwargs)


class Language(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.lang_code = data["lang_code"]
        self.name = data["name"]

    def check(self, client: Client, **kwargs: Any):
        self.assert_not_empty("lang_code")
        self.assert_not_empty("name")
