from unittest import TestCase

import allure

from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from onboarding_physical.tests.steps.hmb.check_phone_steps import step_check_phone
from onboarding_physical.tests.steps.hmb.get_prospect_profile_steps import step_get_prospect_profile
from onboarding_physical.tests.steps.internal.private_contact_steps import step_private_contact
from onboarding_physical.tests.steps.internal.private_prospects_steps import step_private_prospects


class OnboardingPhysicalTC(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext(
            prospect_id='f5cd86b7-836c-4f5b-861b-fcf34021d986',
            iabs_id='4959379',
            phone='998941775859'
        )

    def test_check_phone(self):
        step_check_phone(context=self.context)
        with allure.step("Телефон:"):
            pass

    def test_get_prospect_profile(self):
        step_get_prospect_profile(context=self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    @allure.step("Поиск проспекта по iabsId и номеру телефона")
    def test_prospects(self):
        step_private_prospects(self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass

    @allure.step('Получение контакта')
    def test_private_contact(self):
        step_private_contact(self.context)
        with allure.step(f"({self.context.prospect_id})"):
            pass
