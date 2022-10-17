from unittest import TestCase

import allure

from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext
from onboarding_physical.tests.steps.private_prospects_steps import step_private_prospects


class PrivateProspectsTest(TestCase):

    def setUp(self) -> None:
        self.context = OnboardingPhysicalContext(
            iabs_id="3589246",
            phone="998941775859"
        )

    @allure.step("Поиск проспекта по iabsId и номеру телефона")
    def test_prospects(self):
        step_private_prospects(self.context)

