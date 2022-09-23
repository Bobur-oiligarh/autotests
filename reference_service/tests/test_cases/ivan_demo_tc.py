from unittest import TestCase

import allure

from reference_service.test_data.reference_context import ReferenceServiceContext
from reference_service.tests.steps.card_bins_number_step import card_bins_number_success


class DemoTestCase(TestCase):

    def setUp(self) -> None:
        self.context = ReferenceServiceContext(
            "8600120480409831"
        )

    def test_1(self):
        card_bins_number_success(self.context)

        with allure.step(f"{self.context.card_bins}"):
            pass
