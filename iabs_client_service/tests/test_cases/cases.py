from unittest import TestCase

from iabs_client_service.tests.scenarios.search_clients_scenarios import scenario_search_clients


class DemoScenarioTestCase(TestCase):
    IABSClientID = "4959379"

    def test_iabs_clients_search(self):
        scenario_search_clients(client_uid=self.IABSClientID)
