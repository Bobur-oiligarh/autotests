from unittest import TestCase

import allure

from iabs_client_service.test_data.context import IABSContext
from iabs_client_service.tests.scenarios.search_clients_scenarios import scenario_search_clients
from iabs_client_service.tests.steps.post_clients_search_steps import step_clients_search


class DemoScenarioTestCase(TestCase):

    def setUp(self) -> None:
        self.context = IABSContext(iabs_id="4959379")

    def test_iabs_clients_search(self):
        scenario_search_clients(context=self.context)


class IABSClientTestCase(TestCase):

    def setUp(self) -> None:
        self.context = IABSContext(
            data={
                "number": "0356528",
                "series": "AD",
                "doc_type": "0",
                "pinfl": "31209932580017",
                "tin": "530655303"
            }
        )

    def test_post_clients_search(self):
        step_clients_search(self.context)
