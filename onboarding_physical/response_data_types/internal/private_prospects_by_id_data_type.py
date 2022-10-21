import allure
from abc import ABC
from onboarding_physical.response_data_types.internal.private_contact_response_data_type import PrivateContactDataType
from onboarding_physical.response_data_types.internal.private_prospects_data_type import PrivateProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class PrivateProspectsByIDResponseDataType(PrivateProspectDataType):

    def __init__(self, data: dict):
        super().__init__(data)
        self.doc_type = data['doc_type']
        self.doc_expires_at = data['doc_expiry_date']
        self.doc_issued_at = data['doc_issue_date']
        self.doc_issued_org_code = data['doc_issue_org_code']
        self.doc_issued_org_desc = data['doc_issue_org_desc']
        self.doc_region_code = data['doc_region_code']
        self.doc_district_code = data['doc_district_code']
        self.domicile_address = Address(data['domicile_address']) if data.get('domicile_address') else None
        self.temporary_address = Address(data['temporary_address']) if data.get('temporary_address') else None
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
        self.marital_status = data['marital_status']
        self.is_resident = data['is_resident']
        self.contacts = Contacts(data['contacts'])
        self.first_name_en = data.get('first_name_en')
        self.last_name_en = data.get('last_name_en')
        self.sphere_of_activity = data.get('sphere_of_activity')
        self.subject_state = data.get('subject_state')
        self.tin_registration_date = data.get('tin_registration_date')
        self.tin_registration_gni = data.get('tin_registration_gni')

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

    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_private_prospect_to(obj)

    @allure.step('Установим private_prospect')
    def _set_private_prospect_to(self, obj):
        obj.private_prospect = self


class Contacts(BaseTypeParent):
    def __init__(self, data: list):
        super().__init__()
        self.contacts: list = self.deserialize_to_list_of(PrivateContactDataType, data)

    def check(self, context, **kwargs):
        self.check_list_of("contacts", context, **kwargs)

    def set_data_to(self, obj):
        pass


class Address(BaseType):
    def __init__(self, data):
        super().__init__()
        self.address = data.get('address')
        self.block = data.get('block')
        self.country_code = data.get('country_code')
        self.created_at = data.get('created_at')
        self.district_code = data.get('district_code')
        self.flat = data.get('flat')
        self.house = data.get('house')
        self.id = data.get('id')
        self.kadastr = data.get('kadastr')
        self.place_desc = data.get('place_desc')
        self.profile_id = data.get('profile_id')
        self.region_code = data.get('region_code')
        self.registered_at = data.get('registered_at')
        self.street_desc = data.get('street_desc')
        self.type = data.get('type')

    def check(self, context, **kwargs):
        self.assert_not_empty_str('address')
        self.assert_no_strict_str('block')
        self.assert_no_strict_str('country_code')
        self.assert_no_strict_str('created_at')
        self.assert_no_strict_str('district_code')
        self.assert_no_strict_str('flat')
        self.assert_no_strict_str('house')
        self.assert_no_strict_str('id')
        self.assert_no_strict_str('kadastr')
        self.assert_no_strict_str('place_desc')
        self.assert_no_strict_str('profile_id')
        self.assert_no_strict_str('region_code')
        self.assert_no_strict_str('registered_at')
        self.assert_no_strict_str('street_desc')
        self.assert_no_strict_str('type')
