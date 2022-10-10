import allure

from utils.api_utils.response_data_base import BaseTypeParent


class ProspectProfileResponseType(BaseTypeParent):

    def __init__(self, data):
        super().__init__()
        self.id = data['ID']
        self.source = data['Source']
        self.prospectID = data['ProspectID']
        self.first_name = data['FirstName']
        self.last_name = data['LastName']
        self.middle_name = data['MiddleName']
        self.first_name_en = data['FirstNameEn']
        self.last_name_en = data['LastNameEn']
        self.birth_place = data['BirthPlace']
        self.birth_date = data['BirthDate']
        self.birth_country_code = data['BirthCountryCode']
        self.gender = data['Gender']
        self.tin = data['TIN']
        self.pinfl = data['PINFL']
        self.inps = data['INPS']
        self.nationality_code = data['NationalityCode']
        self.citizenship_code = data['CitizenshipCode']
        self.tin_registration_date = data['TINRegistrationDate']
        self.tin_registration_gni = data['TINRegistrationGNI']
        self.subject_state = data['SubjectState']
        self.marital_status = data['MaritalStatus']
        self.sphere_of_activity = data['SphereOfActivity']
        self.created_at = data['CreatedAt']
        self.updated_at = data['UpdatedAt']
        self.doc_type = data['DocType']
        self.doc_series = data['DocSeries']
        self.doc_number = data['DocNumber']
        self.doc_expires_at = data['DocExpiryDate']
        self.doc_issued_at = data['DocIssueDate']
        self.doc_issued_org_code = data['DocIssueOrgCode']
        self.doc_issued_org_desc = data['DocIssueOrgDesc']
        self.doc_region_code = data['DocRegionCode']
        self.doc_district_code = data['DocDistrictCode']
        self.iabs_id = data['IABSClientID']

    def check(self, context, **kwargs):
        self.assert_not_empty_str('id')
        self.assert_not_empty_int('source')
        self.assert_not_empty_str('prospectID')
        self.assert_not_empty_str('first_name')
        self.assert_not_empty_str('last_name')
        self.assert_not_empty_str('middle_name')
        self.assert_not_empty_str('birth_place')
        self.assert_not_empty_str('birth_date')
        self.assert_not_empty_str('birth_country_code')
        self.assert_not_empty_str('gender')
        self.assert_not_empty_str('tin')
        self.assert_not_empty_str('pinfl')
        self.assert_not_empty_str('inps')
        self.assert_not_empty_str('nationality_code')
        self.assert_not_empty_str('citizenship_code')
        self.assert_not_empty_str('created_at')
        self.assert_not_empty_str('updated_at')
        self.assert_not_empty_str('doc_type')
        self.assert_not_empty_str('doc_series')
        self.assert_not_empty_str('doc_number')
        self.assert_not_empty_str('doc_expires_at')
        self.assert_not_empty_str('doc_issued_at')
        self.assert_not_empty_str('doc_issued_org_code')
        self.assert_not_empty_str('doc_issued_org_desc')
        self.assert_not_empty_str('doc_region_code')

    def set_data_to(self, obj):
        self._set_profile_to(obj)

    def _set_profile_to(self, obj):
        obj.prospect_profile = self

