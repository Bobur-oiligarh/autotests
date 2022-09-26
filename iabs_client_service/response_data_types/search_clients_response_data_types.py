from unittest import TestCase as tc
import allure

from iabs_client_service.test_data.context import IABSContext
from utils.api_utils.response_data_base import BaseType, BaseTypeParent

__all__ = ['IABSClient', 'Branches', 'Branch']


class IABSClient(BaseTypeParent):
    """Creates IABS client class."""

    def __init__(self, data: dict):
        """Initializes IABS client response object attributes. """
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
        self.check_iabs_id()
        self.check_doc_type()
        self.check_doc_series()
        self.check_doc_number()
        self.check_doc_issued_at()
        self.check_doc_expires_at()
        self.check_doc_issued_by()
        self.check_pinfl()
        self.check_tin()
        self.check_last_name()
        self.check_first_name()
        self.check_middle_name()
        self.check_birth_date()
        self.check_birth_country_code()
        self.check_birth_place()
        self.check_gender()
        self.check_citizenship_country_code()
        self.check_branches(context, **kwargs)
        self.check_residence_country_code()
        self.check_residence_region_code()
        self.check_residence_district_code()
        self.check_residence_full_address()

    @allure.step("client_uid - не пустой")
    def check_iabs_id(self):
        tc().assertNotEqual(self.iabs_id, "",
                            f"client_uid ({self.iabs_id}) - пустой" + self.__str__())

    @allure.step("doc_type - не пустой")
    def check_doc_type(self):
        tc().assertNotEqual(self.doc_type, "",
                            f"doc_type ({self.doc_type}) - пустой" + self.__str__())

    @allure.step("doc_series - не пустой")
    def check_doc_series(self):
        tc().assertNotEqual(self.doc_series, "",
                            f"doc_series ({self.doc_series}) - пустой" + self.__str__())

    @allure.step("doc_number - не пустой")
    def check_doc_number(self):
        tc().assertNotEqual(self.doc_number, "",
                            f"doc_number ({self.doc_number}) - пустой" + self.__str__())

    @allure.step("doc_issued_at - не пустой")
    def check_doc_issued_at(self):
        tc().assertNotEqual(self.doc_issued_at, "",
                            f"doc_issued_at ({self.doc_issued_at}) - пустой" + self.__str__())

    @allure.step("doc_expires_at - не пустой")
    def check_doc_expires_at(self):
        tc().assertNotEqual(self.doc_expires_at, "",
                            f"doc_expires_at ({self.doc_expires_at}) - пустой" + self.__str__())

    @allure.step("doc_issued_by - не пустой")
    def check_doc_issued_by(self):
        tc().assertNotEqual(self.doc_issued_by, "",
                            f"doc_issued_by ({self.doc_issued_by}) - пустой" + self.__str__())

    @allure.step("pinfl - не пустой")
    def check_pinfl(self):
        tc().assertNotEqual(self.pinfl, "", f"pinfl ({self.pinfl}) - пустой" + self.__str__())

    @allure.step("tin - не пустой")
    def check_tin(self):
        tc().assertNotEqual(self.tin, "", f"tin ({self.tin}) - пустой" + self.__str__())

    @allure.step("last_name - не пустой")
    def check_last_name(self):
        tc().assertNotEqual(self.last_name, "",
                            f"last_name ({self.last_name}) - пустой" + self.__str__())

    @allure.step("first_name - не пустой")
    def check_first_name(self):
        tc().assertNotEqual(self.first_name, "",
                            f"first_name ({self.first_name}) - пустой" + self.__str__())

    @allure.step("middle_name - не пустой")
    def check_middle_name(self):
        tc().assertNotEqual(self.middle_name, "",
                            f"middle_name ({self.middle_name}) - пустой" + self.__str__())

    @allure.step("birth_date - не пустой")
    def check_birth_date(self):
        tc().assertNotEqual(self.birth_date, "",
                            f"birth_date ({self.birth_date}) - пустой" + self.__str__())

    @allure.step("birth_country_code - не пустой")
    def check_birth_country_code(self):
        tc().assertNotEqual(self.birth_country_code, "",
                            f"birth_country_code ({self.birth_country_code}) - пустой" + self.__str__())

    @allure.step("birth_place - не пустой")
    def check_birth_place(self):
        tc().assertNotEqual(self.birth_place, "",
                            f"birth_place ({self.birth_place}) - пустой" + self.__str__())

    @allure.step("gender - не пустой")
    def check_gender(self):
        tc().assertNotEqual(self.gender, "",
                            f"gender ({self.gender}) - пустой" + self.__str__())

    @allure.step("citizenship_country_code - не пустой")
    def check_citizenship_country_code(self):
        tc().assertNotEqual(self.citizenship_country_code, "",
                            f"citizenship_country_code ({self.citizenship_country_code}) - пустой" + self.__str__())

    @allure.step("branches - не пустой")
    def check_branches(self, iabs_client, **kwargs):
        self.branches.check(iabs_client, **kwargs)

    @allure.step("residence_country_code - не пустой")
    def check_residence_country_code(self):
        tc().assertNotEqual(self.residence_country_code, "",
                            f"residence_country_code ({self.residence_country_code}) - пустой" + self.__str__())

    @allure.step("residence_region_code - не пустой")
    def check_residence_region_code(self):
        tc().assertNotEqual(self.residence_region_code, "",
                            f"residence_region_code ({self.residence_region_code}) - пустой" + self.__str__())

    @allure.step("residence_district_code - не пустой")
    def check_residence_district_code(self):
        tc().assertNotEqual(self.residence_district_code, "",
                            f"residence_district_code ({self.residence_district_code}) - пустой" + self.__str__())

    @allure.step("residence_full_address - не пустой")
    def check_residence_full_address(self):
        tc().assertNotEqual(self.residence_full_address, "",
                            f"residence_full_address ({self.residence_full_address}) - пустой" + self.__str__())

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
        self.check_all_branches(client, **kwargs)

    @allure.step("Проверка параметров всех филлиалов")
    def check_all_branches(self, client: IABSContext, **kwargs):
        for branch in self.branches:
            with allure.step(f"branch {branch.mfo}"):
                branch.check(client, **kwargs)


class Branch(BaseType):
    """Implements bank branch object. """
    def __init__(self, data: dict):
        super().__init__()
        self.mfo = data["mfo"]
        self.client_code = data["client_code"]

    def check(self, client: IABSContext, **kwargs):
        self.check_mfo()
        self.check_client_code()

    @allure.step('mfo - пустой')
    def check_mfo(self):
        self._tc.assertNotEqual(self.mfo, "", f"mfo ({self.mfo}) пустой" + self.__str__())

    @allure.step('client_code - пустой')
    def check_client_code(self):
        self._tc.assertNotEqual(self.client_code, "",
                                f"client_code ({self.client_code}) пустой" + self.__str__())
