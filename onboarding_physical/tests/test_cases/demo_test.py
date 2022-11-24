from unittest import TestCase

import allure

from onboarding_physical.response_data_types.internal.private_address_data_type import PrivateAddress
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from onboarding_physical.tests.steps.hmb.check_phone_steps import step_check_phone
from onboarding_physical.tests.steps.hmb.get_prospect_profile_steps import step_get_prospect_profile
from onboarding_physical.tests.steps.internal.private_address_by_address_id_steps import step_private_address_by_id
from onboarding_physical.tests.steps.internal.private_contact_steps import step_private_contact
from onboarding_physical.tests.steps.internal.private_contacts_steps import step_private_contacts
from onboarding_physical.tests.steps.internal.private_prospects_by_id_steps import step_private_prospect_by_prospect_id
from onboarding_physical.tests.steps.internal.private_prospects_steps import step_private_prospects
from onboarding_physical.tests.steps.internal.put_private_address_to_prospect_steps import \
    step_put_private_address_to_prospect


class PrivateProspectsTest(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext(
            iabs_id="3589246",
            phone="998941775859"
        )

    @allure.step("Поиск проспекта по iabsId и номеру телефона")
    def test_prospects(self):
        step_private_prospects(self.context)


class OnboardingPhysicalTC(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext(
            prospect_id='f5cd86b7-836c-4f5b-861b-fcf34021d986',
            iabs_id='4959379',
            phone='998941775859',
            contact_id='0a699f19-d71b-48b0-8606-4837102c59c2',
            address_id='2056e105-703e-4d60-9af7-055ee56bbf56'
        )
        data = {
            'id': '2056e105-703e-4d60-9af7-055ee56bbf56',
            'profile_id': '964b1484-00d4-4c22-b893-687743ded710',
            'address': 'ТОШКЕНТ ШАҲРИ; ЯШНОБОД ТУМАНИ; г. Ташкент, Яшнабадский район, ул. Авиасозлар, пр. 1, '
                       'Алимкент МСГ, 4- Дом, 10- Квартира',
            'registered_at': '2021-05-04T00:00:00Z',
            'country_code': '860',
            'region_code': '26',
            'district_code': '207',
            'kadastr': '10:04:04:03:01:5005:0001:010',
            'created_at': '2022-04-25T04:01:44.207872Z'
        }
        self.context.private_address = PrivateAddress(data).get_data_to_put_request()

    def test_check_phone(self):
        step_check_phone(context=self.context)
        with allure.step("Телефон:"):
            pass

    def test_get_prospect_profile(self):
        step_get_prospect_profile(context=self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    def test_prospects(self):
        step_private_prospects(self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    @allure.step('Получение контакта')
    def test_private_contact(self):
        step_private_contact(self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    def test_private_contacts(self):
        step_private_contacts(self.context)
        with allure.step(f"({self.context.contact_id})"):
            pass

    def test_private_prospects_by_prospect_id(self):
        step_private_prospect_by_prospect_id(self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    def test_private_address_by_address_id(self):
        step_private_address_by_id(self.context)
        with allure.step(f"({self.context.prospect_id}"):
            pass

    def test_put_private_address_to_prospect(self):
        step_put_private_address_to_prospect(self.context)
