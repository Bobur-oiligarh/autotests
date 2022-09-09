from abc import ABC

import allure

from api_mobile.response_data_types.references.atm import Coordinates, DiffLangTextParams
from api_mobile.response_data_types.response_data_base import BaseType


class Branch(BaseType, ABC):
    """Implements branch object."""
    def __init__(self, data: dict):
        """Initializes branch object attributes.
        :param data: dict
        """
        super().__init__()
        self.mfo = data['mfo']
        self.Coords = Coordinates(data['Coords'])
        self.region_code = data['region_code']
        self.is_open = data['is_open']
        self.weekends = DiffLangTextParams(data['weekends'])
        self.services = DiffLangTextParams(data['services'])
        self.address = DiffLangTextParams(data['address'])
        self.work_time = DiffLangTextParams(data['work_time'])
        self.lunch_time = DiffLangTextParams(data['lunch_time'])
        self.status_text = DiffLangTextParams(data['status_text'])

    def check(self, client, **kwargs):
        self.check_mfo_is_not_empty()
        self.check_coords_is_not_empty(client, **kwargs)
        self.check_region_code_is_not_empty()
        self.check_is_open_field_is_not_empty()
        self.check_weekends_is_not_empty(client, **kwargs)

    @allure.step('Поле МФО - не пустой.')
    def check_mfo_is_not_empty(self):
        self._tc.assertNotEqual(self.mfo, "",
                                f"mfo ({self.mfo}) пустой" + self.__str__())

    @allure.step('Поле координаты - не пустой.')
    def check_coords_is_not_empty(self, client, **kwargs):
        self.Coords.check(client, **kwargs)

    @allure.step('Поле регион  - не пустой.')
    def check_region_code_is_not_empty(self):
        self._tc.assertNotEqual(self.region_code, "",
                                f"region_code ({self.region_code}) пустой" + self.__str__())

    @allure.step('Поле открыто - не пустой.')
    def check_is_open_field_is_not_empty(self):
        self._tc.assertNotEqual(self.is_open, "",
                                f"is_open ({self.is_open}) пустой" + self.__str__())

    @allure.step('Поле выходные дни - не пустой.')
    def check_weekends_is_not_empty(self, client, **kwargs):
        self.weekends.check(client, **kwargs)











"""
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

"""

    """
    {
    "status": "Success",
    "error_code": 0,
    "error_note": "",
    "data": [
        {
            "title": "Каршинский филиал",
            "mfo": "30000",
            "region_code": "10",
            "Coords": {
                "lat": "38.8545089",
                "lng": "65.792429"
            },
            "weekends": {
                "uz": "Shanba, Yakshanba",
                "cy": "",
                "ru": "Суббота, Воскресенье",
                "en": ""
            },
            "services": {
                "uz": "Kreditlar, omonatlar, milliy va xalqaro plastik kartalar, milliy va xalqaro pul o'tkazmalari, depozit yacheykalar, Valyuta ayirboshlash xizmatlari, Юmoney elektron hamyon uchun identifikatsiyadan o'tish",
                "cy": "",
                "ru": "Кредиты, депозиты, национальные и международные пластиковые карты, денежные переводы, депозитные ячейки, Валютно-обменные операции, Прохождение идентификации для ЮMoney",
                "en": ""
            },
            "address": {
                "uz": "Qarshi shahri, A Temur ko'chasi,  41 - uy",
                "cy": "",
                "ru": " г. Карши, ул. А Темур, 41 ",
                "en": ""
            },
            "work_time": {
                "uz": "Dush-Jum 9:00-17:00",
                "cy": "",
                "ru": "Пон-Пят 9:00-17:00 ",
                "en": ""
            },
            "lunch_time": "12:30-13:30",
            "status_text": {
                "uz": "17:00 gacha ochiq",
                "cy": "",
                "ru": "Открыто до 17:00",
                "en": "Open until 05:00 PM"
            },
            "is_open": true
        },
    """




