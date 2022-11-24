import allure
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
    def _set_atms(self, context):
        context.atm_list = self

    def check(self, context, **kwargs):
        self.check_list_of("atm_list", context, **kwargs)


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

    def check(self, context, **kwargs):
        self.assert_not_none_and_true_type("mfo", str)
        self.assert_not_empty_str("type")
        self.check_attrs_of("Coords", context, **kwargs)
        self.assert_not_empty_str("region_code")
        self.check_attrs_of("orienter", context, **kwargs)
        self.check_attrs_of("work_time", context, **kwargs)
        self.check_attrs_of("work_days", context, **kwargs)
        self.check_attrs_of("atm_type", context, **kwargs)
        self.check_attrs_of("address", context, **kwargs)


class Coordinates(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.lat = data["lat"]
        self.lng = data["lng"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("lat")
        self.assert_not_empty_str("lng")


class DiffLangTextParams(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.uz = data["uz"]
        self.ru = data["ru"]

    def check(self, context, **kwargs):
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
