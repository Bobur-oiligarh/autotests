from typing import Any
import allure
from back_mobile.response_data_types.references.atm import Coordinates, DiffLangTextParams
from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "AvailableBranches",
    "Branch"
]


class AvailableBranches(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.branches_list: list = self.deserialize_to_list_of(Branch, data)

    def set_data_to(self, obj: Client):
        self._set_branches(obj)

    @allure.step("Установить филиалы клиенту.")
    def _set_branches(self, client: Client):
        client.branches = self

    def check(self, client: Client, **kwargs):
        self.check_all_branches(client, **kwargs)

    @allure.step("Проверка параметров всех филлиалов.")
    def check_all_branches(self, client: Client, **kwargs):
        for branch in self.branches_list:
            with allure.step(f"branch {branch.mfo}"):
                branch.check(client, **kwargs)


class Branch(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.mfo = data['mfo']
        self.Coords = Coordinates(data['Coords'])
        self.region_code = data['region_code']
        self.is_open = data['is_open']
        self.weekends = DiffLangTextParams(data['weekends'])
        self.services = DiffLangTextParams(data['services'])
        self.address = DiffLangTextParams(data['address'])
        self.work_time = DiffLangTextParams(data['work_time'])
        self.lunch_time = data['lunch_time']
        self.status_text = DiffLangTextParams(data['status_text'])

    def check(self, client: Client, **kwargs):
        self.assert_not_empty("mfo")
        self.check_attrs_of("Coords", client, **kwargs)
        self.assert_not_empty("region_code")
        self.assert_not_empty("is_open")
        self.check_attrs_of("weekends", client, **kwargs)
        self.check_attrs_of("services", client, **kwargs)
        self.check_attrs_of("address", client, **kwargs)
        self.check_attrs_of("work_time", client, **kwargs)
        self.assert_not_empty("lunch_time")
        self.check_attrs_of("status_text", client, **kwargs)
