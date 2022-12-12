from unittest import TestCase

from sme_credits.tests.scenarios.vbnv_116_scenario import vbnv_116_scenario


class VBNV116TestCase(TestCase):

    def test_vbnv_116_scenario(self):
        vbnv_116_scenario(self.context)

