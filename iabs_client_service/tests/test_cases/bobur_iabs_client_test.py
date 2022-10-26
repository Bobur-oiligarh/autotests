from unittest import TestCase

import allure

from iabs_client_service.test_data import IABSContext
from iabs_client_service.tests.steps.post_clients_search_steps import step_post_clients_search


class IABSClientTestCase(TestCase):

    def SetUp(self) -> None:
        self.context = IABSContext(
            data={
                "doc_number": "0356528",
                "doc_series": "AD",
                "doc_type": "0",
                "pinfl": "31209932580017",
                "tin": "530655303"
            }
        )

    def test_post_clients_search(self):
        step_post_clients_search(self.context)
        with allure.step(f"{self.context.iabs_id}"):
            pass
