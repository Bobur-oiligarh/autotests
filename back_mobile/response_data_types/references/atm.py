from typing import Any
import allure
from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = [
    "ATMs",
    "ATM",
    "Coordinates",
    "DiffLangTextParams"
]


class ATMs(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.atm_list: list = self.deserialize_to_list_of(ATM, data)

    def set_data_to(self, obj):
        self._set_atms(obj)

    @allure.step("Установить банкоматы клиенту")
    def _set_atms(self, client):
        client.atm_list = self

    def check(self, client, **kwargs):
        self.check_list_of("atm_list", client, **kwargs)


class ATM(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.mfo = data["mfo"]
        self.type = data["type"]
        self.Coords = Coordinates(data["Coords"])
        self.region_code = data["region_code"]
        self.orienter = DiffLangTextParams(data["orienter"])
        self.work_time = DiffLangTextParams(data["work_time"])
        self.work_days = DiffLangTextParams(data["work_days"])
        self.atm_type = DiffLangTextParams(data["atm_type"])
        self.address = DiffLangTextParams(data["address"])

    def check(self, client, **kwargs):
        self.assert_not_none_and_true_type("mfo", str)
        self.assert_not_empty_str("type")
        self.check_attrs_of("Coords", client, **kwargs)
        self.assert_not_empty_str("region_code")
        self.check_attrs_of("orienter", client, **kwargs)
        self.check_attrs_of("work_time", client, **kwargs)
        self.check_attrs_of("work_days", client, **kwargs)
        self.check_attrs_of("atm_type", client, **kwargs)
        self.check_attrs_of("address", client, **kwargs)


class Coordinates(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.lat = data["lat"]
        self.lng = data["lng"]

    def check(self, client, **kwargs):
        self.assert_not_empty_str("lat")
        self.assert_not_empty_str("lng")


class DiffLangTextParams(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.uz = data["uz"]
        self.ru = data["ru"]

    def check(self, client: Client, **kwargs):
        self.uz_not_null()
        self.ru_not_null()

    @allure.step("Текст на узбекском языке не пустой")
    def uz_not_null(self):
        self._tc.assertNotEqual(self.uz, "",
                                f"Текст на узбекском языке ({self.uz}) пустой" + self.__str__())

    @allure.step("Текст на русском языке не пустой")
    def ru_not_null(self):
        self._tc.assertNotEqual(self.ru, "",
                                f"Текст на русском языке ({self.ru}) пустой" + self.__str__())
