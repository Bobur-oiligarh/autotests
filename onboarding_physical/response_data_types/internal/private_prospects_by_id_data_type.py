import allure

from onboarding_physical.response_data_types.internal.private_prospects_data_type import PrivateProspectDataType
from utils.api_utils.response_data_base import BaseType


class PrivateProspectsByIDResponseDataType(PrivateProspectDataType):

    def __init__(self, data: dict):
        super().__init__()
        self.contact_id = None
        self.doc_type = data['doc_type']
        self.doc_expires_at = data['doc_expiry_date']
        self.doc_issued_at = data['doc_issue_date']
        self.doc_issued_org_code = data['doc_issue_org_code']
        self.doc_issued_org_desc = data['doc_issue_org_desc']
        self.doc_region_code = data['doc_region_code']
        self.doc_district_code = data['doc_district_code']
        self.domicile_address = DomicileAddress(data['domicile_address'])


class DomicileAddress(BaseType):

    def __init__(self, data):
        super().__init__()
        self.id = data['id']
        self.profile_id = data['profile_id']
        self.address = data['address']
        self.registered_at = data['registered_at']
        self.country_code = data['country_code']
        self.region_code = data['region_code']
        self.district_code = data['district_code']
        self.kadastr = data['kadastr']
        self.created_at = data['created_at']

    def check(self, context, **kwargs):
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('profile_id')
        self.assert_not_empty_str('address')
        self.assert_not_empty_str('registered_at')
        self.assert_not_empty_str('country_code')
        self.assert_not_empty_str('region_code')
        self.assert_not_empty_str('district_code')
        self.assert_not_empty_str('kadastr')
        self.assert_not_empty_str('created_at')