from typing import Any
from unittest import TestCase as tc
import allure

from back_mobile.test_data.client import Client
from utils.api_utils.response_data_base import BaseType


class IABSClient(BaseType):
    """Creates IABS client class."""

    def __init__(self, data: dict):
        """Initializes IABS client response object attributes. """
        super().__init__()
        self.client_uid = data['client_uid']
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
        self.branches = data['branches']
        self.residence_country_code = data['residence_country_code']
        self.residence_region_code = data['residence_region_code']
        self.residence_district_code = data['residence_district_code']
        self.residence_full_address = data['residence_full_address']
        self.residence_kadastr = data['residence_kadastr']

    def check(self, client: Client = None, **kwargs: Any):
        self.client_uid()
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
        self.check_branches()
        self.check_residence_country_code()
        self.check_residence_region_code()
        self.check_residence_district_code()
        self.check_residence_full_address()

    @allure.step("client_uid - не пустой")
    def check_client_uid(self):
        tc().assertNotEqual(self.client_uid, "",
                            f"client_uid ({self.client_uid}) - пустой" + self.__str__())

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
    def check_branches(self):
        tc().assertNotEqual(self.branches, "", f"branches ({self.branches}) - пустой" + self.__str__())

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

