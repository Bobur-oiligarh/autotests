import allure
from back_mobile.response_data_types.references.atm import Coordinates, DiffLangTextParams
from utils.api_utils.response_data_base import BaseTypeParent, BaseType

__all__ = [
    "AvailableBranches",
    "Branch"
]


class AvailableBranches(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.branches_list: list = self.deserialize_to_list_of(Branch, data)

    def set_data_to(self, obj):
        self._set_branches(obj)

    @allure.step("Установить филиалы клиенту.")
    def _set_branches(self, context):
        context.branches = self

    def check(self, context, **kwargs):
        self.check_list_of("branches_list", context, **kwargs)


class Branch(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.title = data["title"]
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

    def check(self, context, **kwargs):
        self.assert_not_empty_str("title")
        self.assert_not_empty_str("mfo")
        self.check_attrs_of("Coords", context, **kwargs)
        self.assert_not_empty_str("region_code")
        self.assert_not_empty_bool("is_open")
        self.check_attrs_of("weekends", context, **kwargs)
        self.check_attrs_of("services", context, **kwargs)
        self.check_attrs_of("address", context, **kwargs)
        self.check_attrs_of("work_time", context, **kwargs)
        self.assert_not_empty_str("lunch_time")
        self.check_attrs_of("status_text", context, **kwargs)
