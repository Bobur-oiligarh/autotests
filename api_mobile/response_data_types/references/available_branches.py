from typing import Any

import allure

from api_mobile.response_data_types.references.atm import Coordinates, DiffLangTextParams
from api_mobile.response_data_types.response_data_base import BaseType, BaseTypeParent
from api_mobile.test_data.client import Client


class AvailableBranches(BaseTypeParent):
    """Implements available branches. """
    def __init__(self, data: list):
        super().__init__()
        self.branches_list: list = self.deserialize_to_list_of(Branch, data)

    def set_data_to(self, obj: Client):
        self._set_branches(obj)

    @allure.step("Установить филиалы клиенту.")
    def _set_branches(self, client: Client):
        client.branches_list = self

    def check(self, client: Client, **kwargs: Any):
        self.check_all_branches(client, **kwargs)

    @allure.step("Проверка параметров всех филлиалов.")
    def check_all_branches(self, client: Client, **kwargs: Any):
        i = 0
        for branch in self.branches_list:
            with allure.step(f"branch {i}"):
                branch.check(client, **kwargs)


class Branch(BaseType):
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
        self.check_mfo()
        self.check_coords(client, **kwargs)
        self.check_region_code()
        self.check_is_open()
        self.check_weekends(client, **kwargs)
        self.check_services(client, **kwargs)
        self.check_address(client, **kwargs)
        self.check_work_time(client, **kwargs)
        self.check_lunch_time()
        self.check_status_text(client, **kwargs)

    @allure.step('mfo - не пустой.')
    def check_mfo(self):
        self._tc.assertNotEqual(self.mfo, "",
                                f"mfo ({self.mfo}) пустой" + self.__str__())

    @allure.step('Coords - не пустой.')
    def check_coords(self, client, **kwargs):
        self.Coords.check(client, **kwargs)

    @allure.step('region_code - не пустой.')
    def check_region_code(self):
        self._tc.assertNotEqual(self.region_code, "",
                                f"region_code ({self.region_code}) пустой" + self.__str__())

    @allure.step('is_open - не пустой.')
    def check_is_open(self):
        self._tc.assertNotEqual(self.is_open, "",
                                f"is_open ({self.is_open}) пустой" + self.__str__())

    @allure.step('weekends - не пустой.')
    def check_weekends(self, client, **kwargs):
        self.weekends.check(client, **kwargs)

    @allure.step('services - не пустой.')
    def check_services(self, client, **kwargs):
        self.services.check(client, **kwargs)

    @allure.step('address - не пустой.')
    def check_address(self, client, **kwargs):
        self.address.check(client, **kwargs)

    @allure.step('work_time - не пустой.')
    def check_work_time(self, client, **kwargs):
        self.work_time.check(client, **kwargs)

    @allure.step('lunch_time - не пустой.')
    def check_lunch_time(self):
        self._tc.assertNotEqual(self.lunch_time, "",
                                f"lunch_time ({self.lunch_time}) пустой" + self.__str__())

    @allure.step('status_text - не пустой.')
    def check_status_text(self, client, **kwargs):
        self.status_text.check(client, **kwargs)


