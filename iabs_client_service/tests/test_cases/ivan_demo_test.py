from unittest import TestCase

from iabs_client_service.test_data import IABSContext
from iabs_client_service.tests.scenarios import scenario_search_clients


class DemoScenarioTestCase(TestCase):

    def setUp(self) -> None:
        self.context = IABSContext(iabs_id="4959379")

    def test_iabs_clients_search(self):
        scenario_search_clients(context=self.context)
