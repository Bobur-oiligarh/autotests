from unittest import TestCase

import allure

from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from onboarding_physical.tests.steps.check_phone_steps import step_check_phone


class OnboardingPhysicalTC(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext()

    def test_check_phone(self):
        step_check_phone(context=self.context)
        print(self.context.prospectId)
        with allure.step("Телефон:"):
            pass