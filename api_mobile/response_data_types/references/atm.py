import allure

from utils.api_utils.response_data_base import BaseType, BaseTypeParent


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
        self.check_all_atms(client, **kwargs)

    @allure.step("Проверка параметров всех банкоматов")
    def check_all_atms(self, client, **kwargs):
        i = 0
        for atm in self.atm_list:
            with allure.step(f"atm {i}"):
                atm.check(client, **kwargs)
            i += 1



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
        self.type_not_empty()
        self.check_coords(client, **kwargs)
        self.region_code_not_empty()
        self.check_orienter(client, **kwargs)
        self.check_work_time(client, **kwargs)
        self.check_work_days(client, **kwargs)
        self.check_atm_type(client, **kwargs)
        self.check_address(client, **kwargs)

    @allure.step("type не пустой")
    def type_not_empty(self):
        self._tc.assertNotEqual(self.type, "",
                                f"type ({self.type}) пустой" + self.__str__())

    @allure.step("Coords не пустой")
    def check_coords(self, client, **kwargs):
        self.Coords.check(client, **kwargs)

    @allure.step("region_code не пустой")
    def region_code_not_empty(self):
        self._tc.assertNotEqual(self.region_code, "",
                                f"region_code ({self.region_code}) пустой" + self.__str__())

    @allure.step("проверка параметров orienter")
    def check_orienter(self, client, **kwargs):
        self.orienter.check(client, **kwargs)

    @allure.step("проверка параметров work_time")
    def check_work_time(self, client, **kwargs):
        self.work_time.check(client, **kwargs)

    @allure.step("проверка параметров work_days")
    def check_work_days(self, client, **kwargs):
        self.work_days.check(client, **kwargs)

    @allure.step("проверка параметров atm_type")
    def check_atm_type(self, client, **kwargs):
        self.atm_type.check(client, **kwargs)

    @allure.step("проверка параметров address")
    def check_address(self, client, **kwargs):
        self.address.check(client, **kwargs)


class Coordinates(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.lat = data["lat"]
        self.lng = data["lng"]

    def check(self, client, **kwargs):
        self.lat_not_empty()
        self.lng_not_empty()

    @allure.step("lat не пустой")
    def lat_not_empty(self):
        self._tc.assertNotEqual(self.lat, "",
                                f"lat ({self.lat}) пустой" + self.__str__())

    @allure.step("lng не пустой")
    def lng_not_empty(self):
        self._tc.assertNotEqual(self.lng, "",
                                f"lng ({self.lng}) пустой" + self.__str__())


class DiffLangTextParams(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.uz = data["uz"]
        self.ru = data["ru"]

    def check(self, client, **kwargs):
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
