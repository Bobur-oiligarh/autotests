import allure
from abc import ABC
from onboarding_physical.response_data_types.internal.private_contact_response_data_type import PrivateContactDataType
from onboarding_physical.response_data_types.internal.private_prospects_data_type import PrivateProspectDataType
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from utils.api_utils.response_data_base import BaseType, BaseTypeParent


class PrivateProspectsByIDResponseDataType(PrivateProspectDataType):

    def __init__(self, data: dict):
        super().__init__(data)
        if data.get('contact_id'):
            super().contact_id = data['contact_id']
        else:
            super().contact_id = None
        self.doc_type = data['doc_type']
        self.doc_expires_at = data['doc_expiry_date']
        self.doc_issued_at = data['doc_issue_date']
        self.doc_issued_org_code = data['doc_issue_org_code']
        self.doc_issued_org_desc = data['doc_issue_org_desc']
        self.doc_region_code = data['doc_region_code']
        self.doc_district_code = data['doc_district_code']
        self.domicile_address = DomicileAddress(data['domicile_address'])
        self.temporary_address = TemporaryAddress(data['temporary_address'])
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

        if data.get("first_name_en"):
            self.first_name_en = data['first_name_en']

        if data.get("last_name_en"):
            self.first_name_en = data['last_name_en']

        if data.get("sphere_of_activity"):
            self.first_name_en = data['sphere_of_activity']

        if data.get("subject_state"):
            self.first_name_en = data['subject_state']

        if data.get("tin_registration_date"):
            self.first_name_en = data['tin_registration_date']

        if data.get("tin_registration_gni"):
            self.first_name_en = data['tin_registration_gni']

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_str('doc_type')
        self.assert_not_empty_str('doc_expiry_date')
        self.assert_not_empty_str('doc_issue_date')
        self.assert_not_empty_str('doc_issue_org_code')
        self.assert_not_empty_str('doc_issue_org_desc')
        self.assert_not_empty_str('doc_region_code')
        self.domicile_address.check(context, **kwargs)
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
        self.assert_not_empty_str('contact_id')
        self.assert_not_empty_str('first_name_en')
        self.assert_not_empty_str('last_name_en')
        self.assert_not_empty_str('sphere_of_activity')
        self.assert_not_empty_str('subject_state')
        self.assert_not_empty_str('tin_registration_date')
        self.assert_not_empty_str('tin_registration_gni')

    def set_data_to(self, obj: OnboardingPhysicalContext):
        self._set_private_prospect_to(obj)

    @allure.step('Установим private_prospect')
    def _set_private_prospect_to(self, obj):
        obj.private_prospect = self


class Contacts(BaseTypeParent, ABC):

    def __init__(self, data: list):
        super().__init__()
        self.contacts: list = self.deserialize_to_list_of(PrivateContactDataType, data)

    def check(self, context, **kwargs):
        self.check_list_of("contacts", context, **kwargs)


class TemporaryAddress(BaseType):

    def __init__(self, data):
        super().__init__()
        self.address = data['address']
        self.block = data['block']
        self.country_code = data['country_code']
        self.created_at = data['created_at']
        self.district_code = data['district_code']
        self.flat = data['flat']
        self.house = data['house']
        self.id = data['id']
        self.kadastr = data['kadastr']
        self.place_desc = data['place_desc']
        self.profile_id = data['profile_id']
        self.region_code = data['region_code']
        self.registered_at = data['registered_at']
        self.street_desc = data['street_desc']
        self.type = data['type']

    def check(self, context, **kwargs):
        self.assert_not_empty_str('address')
        self.assert_not_empty_str('block')
        self.assert_not_empty_str('country_code')
        self.assert_not_empty_str('created_at')
        self.assert_not_empty_str('district_code')
        self.assert_not_empty_str('flat')
        self.assert_not_empty_str('house')
        self.assert_not_empty_str('id')
        self.assert_not_empty_str('kadastr')
        self.assert_not_empty_str('place_desc')
        self.assert_not_empty_str('profile_id')
        self.assert_not_empty_str('region_code')
        self.assert_not_empty_str('registered_at')
        self.assert_not_empty_str('street_desc')
        self.assert_not_empty_int('type')


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
