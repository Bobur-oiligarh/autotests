from typing import Any
import allure
from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class AvailableLanguages(BaseTypeParent):
    """Provides list of language objects. """

    def __init__(self, data: list):
        super().__init__()
        self.lang_list: list = self.deserialize_to_list_of(Language, data)

    def set_data_to(self, obj):
        self.set_langs(obj)

    def set_langs(self, client):
        client.lang_list = self

    def check(self, client, **kwargs):
        self.check_all_languages(client, **kwargs)

    def check_all_languages(self, client, **kwargs):
        for lang in self.lang_list:
            with allure.step(f"Проверка параметров lang {lang.name}"):
                lang.check(client, **kwargs)


class Language(BaseType):
    """Creates class of language type. """

    def __init__(self, data: dict):
        super().__init__()
        self.lang_code = data["lang_code"]
        self.name = data["name"]

    def check(self, client: Client, **kwargs: Any):
        self.lang_code_not_empty()
        self.name_not_empty()

    @allure.step("lang_code не пустой")
    def lang_code_not_empty(self):
        self._tc.assertNotEqual(self.lang_code, "",
                                f"lang_code ({self.lang_code}) пустой" + self.__str__())

    @allure.step("name не пустой")
    def name_not_empty(self):
        self._tc.assertNotEqual(self.name, "",
                                f"name ({self.name}) пустой" + self.__str__())
