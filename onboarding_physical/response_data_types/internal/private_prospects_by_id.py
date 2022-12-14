import allure

from onboarding_physical.response_data_types.internal.private_address import PrivateAddress
from onboarding_physical.response_data_types.internal.private_contact import PrivateContact
from onboarding_physical.response_data_types.internal.private_prospects import PrivateProspect
from utils.api_utils.response_data_base import BaseTypeParent


class PrivateProspectsByID(PrivateProspect):

    def __init__(self, data: dict):
        super().__init__(data)
        self.doc_type = data['doc_type']
        self.doc_expires_at = data['doc_expiry_date']
        self.doc_issued_at = data['doc_issue_date']
        self.doc_issued_org_code = data['doc_issue_org_code']
        self.doc_issued_org_desc = data['doc_issue_org_desc']
        self.doc_region_code = data['doc_region_code']
        self.doc_district_code = data['doc_district_code']
        self.domicile_address = PrivateAddress(data['domicile_address']) if data.get('domicile_address') else None
        self.temporary_address = PrivateAddress(data['temporary_address']) if data.get('temporary_address') else None
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.middle_name = data['middle_name']
        self.birth_place = data['birth_place']
        self.birth_country_code = data['birth_country_code']
        self.gender = data['gender']
        self.tin = data['tin']
        self.inps = data['inps']
        self.nationality_code = data['nationality_code']
        self.citizenship_code = data['citizenship_code']
        self.is_resident = data['is_resident']
        self.contacts = Contacts(data['contacts'])
        self.first_name_en = data.get('first_name_en')
        self.last_name_en = data.get('last_name_en')
        self.sphere_of_activity = data.get('sphere_of_activity')
        self.subject_state = data.get('subject_state')
        self.tin_registration_date = data.get('tin_registration_date')
        self.tin_registration_gni = data.get('tin_registration_gni')
        self.marital_status = data.get('marital_status')

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_str('doc_type')
        self.assert_not_empty_str('doc_expires_at')
        self.assert_not_empty_str('doc_issued_at')
        self.assert_not_empty_str('doc_issued_org_code')
        self.assert_not_empty_str('doc_issued_org_desc')
        self.assert_not_empty_str('doc_region_code')
        self.domicile_address.check(context, **kwargs)
        if self.temporary_address:
            self.temporary_address.check(context, **kwargs)
        self.assert_not_empty_str('first_name')
        self.assert_not_empty_str('last_name')
        self.assert_not_empty_str('middle_name')
        self.assert_not_empty_str('birth_place')
        self.assert_not_empty_str('birth_country_code')
        self.assert_not_empty_str('gender')
        self.assert_not_empty_str('tin')
        self.assert_not_empty_str('inps')
        self.assert_not_empty_str('nationality_code')
        self.assert_not_empty_str('citizenship_code')
        self.assert_not_empty_bool('is_resident')
        self.contacts.check(context, **kwargs)
        self.assert_no_strict_str('contact_id')
        self.assert_no_strict_str('first_name_en')
        self.assert_no_strict_str('last_name_en')
        self.assert_no_strict_str('sphere_of_activity')
        self.assert_no_strict_str('subject_state')
        self.assert_no_strict_str('tin_registration_date')
        self.assert_no_strict_str('tin_registration_gni')

    def set_data_to(self, obj):
        self._set_private_prospect_to(obj)

    @allure.step('?????????????????? private_prospect')
    def _set_private_prospect_to(self, obj):
        obj.private_prospect = self


class Contacts(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.contacts: list = self.deserialize_to_list_of(PrivateContact, data)

    def check(self, context, **kwargs):
        self.check_list_of("contacts", context, **kwargs)

    def set_data_to(self, obj):
        pass
