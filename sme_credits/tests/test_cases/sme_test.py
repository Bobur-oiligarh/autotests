from unittest import TestCase

import allure

from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.steps.sme_accounts_steps import step_sme_accounts


class SMETestCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()

    def test_sme_accounts(self):
        step_sme_accounts(self.context)
