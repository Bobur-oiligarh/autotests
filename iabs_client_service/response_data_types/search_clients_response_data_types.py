from unittest import TestCase as tc
import allure

from iabs_client_service.test_data.context import IABSContext
from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = ['IABSClient', 'Branches', 'Branch']


class IABSClient(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.iabs_id = data['client_uid']
        self.doc_type = data['doc_type']
        self.doc_series = data['doc_series']
        self.doc_number = data['doc_number']
        self.doc_issued_at = data['doc_issued_at']
        self.doc_expires_at = data['doc_expires_at']
        self.doc_issued_by = data['doc_issued_by']
        self.pinfl = data['pinfl']
        self.tin = data['tin']
        self.last_name = data['last_name']
        self.first_name = data['first_name']
        self.middle_name = data['middle_name']
        self.birth_date = data['birth_date']
        self.birth_country_code = data['birth_country_code']
        self.birth_place = data['birth_place']
        self.gender = data['gender']
        self.citizenship_country_code = data['citizenship_country_code']
        self.marital_status = data['marital_status']
        self.branches = Branches(data['branches'])
        self.residence_country_code = data['residence_country_code']
        self.residence_region_code = data['residence_region_code']
        self.residence_district_code = data['residence_district_code']
        self.residence_full_address = data['residence_full_address']
        self.residence_kadastr = data['residence_kadastr']

    def check(self, context: IABSContext, **kwargs):
        self.assert_not_empty('iabs_id')
        self.assert_not_empty('doc_type')
        self.assert_not_empty('doc_series')
        self.assert_not_empty('doc_number')
        self.assert_not_empty('doc_issued_at')
        self.assert_not_empty('doc_expires_at')
        self.assert_not_empty('doc_issued_by')
        self.assert_not_empty('pinfl')
        self.assert_not_empty('tin')
        self.assert_not_empty('last_name')
        self.assert_not_empty('first_name')
        self.assert_not_empty('middle_name')
        self.assert_not_empty('birth_date')
        self.assert_not_empty('birth_country_code')
        self.assert_not_empty('birth_place')
        self.assert_not_empty('gender')
        self.assert_not_empty('citizenship_country_code')
        self.check_attrs_of('branches', context, **kwargs)
        self.assert_not_empty('residence_country_code')
        self.assert_not_empty('residence_region_code')
        self.assert_not_empty('residence_district_code')
        self.assert_not_empty('residence_full_address')

    def set_data_to(self, obj: IABSContext):
        self._set_iabs_client(obj)

    @allure.step("Установим клиента iabs")
    def _set_iabs_client(self, obj: IABSContext):
        obj.iabs_client = self


class Branches(BaseTypeParent):
    """Provides list of bank branches objects list. """
    def __init__(self, data: list):
        super().__init__()
        self.branches = self.deserialize_to_list_of(Branch, data)

    def set_data_to(self, obj: IABSContext):
        self._set_branches_to_iabs_client(obj)

    @allure.step("Установить филлиалы клиенту")
    def _set_branches_to_iabs_client(self, obj):
        obj.branches = self

    def check(self, client, **kwargs):
        self.check_list_of('branches', client, **kwargs)


class Branch(BaseType):
    """Implements bank branch object. """
    def __init__(self, data: dict):
        super().__init__()
        self.mfo = data["mfo"]
        self.client_code = data["client_code"]

    def check(self, client: IABSContext, **kwargs):
        self.assert_not_empty('mfo')
        self.assert_not_empty('client_code')
