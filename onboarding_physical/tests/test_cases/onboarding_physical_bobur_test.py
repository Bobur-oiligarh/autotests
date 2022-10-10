from unittest import TestCase

import allure

from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from onboarding_physical.tests.steps.check_phone_steps import step_check_phone


class OnboardingPhysicalTC(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext(
            prospectID='f5cd86b7-836c-4f5b-861b-fcf34021d986'
        )

    def test_check_phone(self):
        step_check_phone(context=self.context)
        print(self.context.prospectID)
        with allure.step("Телефон:"):
            pass

    def test_get_prospect_profile(self):
        step_get_prospect_profile(context=self.context)
        with allure.step(f"({self.context.prospectID})"):
            pass
