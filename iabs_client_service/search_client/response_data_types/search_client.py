from utils.api_utils.response_data_base import BaseType


class IABSClient(BaseType):
    """Creates IABS client class."""

    def __init__(self, client_id):
        self.client_uid = client_id
        self.doc_type = None
        self.doc_series = None
        self.doc_number = None
        self.doc_issued_at = None
        self.doc_expires_at = None
        self.doc_issued_by = None
        self.pinfl = None
        self.tin = None
        self.last_name = None
        self.first_name = None
        self.middle_name = None
        self.birth_date = None
        self.birth_country_code = None
        self.birth_place = None
        self.gender = None
        self.citizenship_country_code = None
        self.marital_status = None
        self.branches = None
        self.residence_country_code = None
        self.residence_region_code = None
        self.residence_district_code = None
        self.residence_full_address = None
        self.residence_kadastr = None

    def check(self, client: IABSClient, **kwargs):
        pass


"""
"client_uid": "4959379",
        "doc_type": "0",
        "doc_series": "AD",
        "doc_number": "0356528",
        "doc_issued_at": "2021-05-04",
        "doc_expires_at": "2031-05-03",
        "doc_issued_by": "Qashqadaryo vil dexkonobod tumani IIB",
        "pinfl": "31209932580017",
        "tin": "530655303",
        "last_name": "KHUSANOV",
        "first_name": "MAKSADALI",
        "middle_name": "KHOLMAMATOVICH",
        "birth_date": "1993-09-12",
        "birth_country_code": "860",
        "birth_place": "Qashqadaryo vil dexkonobod tumani",
        "gender": "1",
        "citizenship_country_code": "860",
        "marital_status": "",
        "branches": [
            {
                "mfo": "01031",
                "client_code": "62229552"
            },
            {
                "mfo": "00083",
                "client_code": "62229552"
            },
            {
                "mfo": "01008",
                "client_code": "62229552"
            }
        ],
        "residence_country_code": "860",
        "residence_region_code": "10",
        "residence_district_code": "046",
        "residence_full_address": "Qashqadaryo vil dexkonobod tumani Boyqurgon",
        "residence_kadastr": ""
"""