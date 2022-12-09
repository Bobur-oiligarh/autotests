from unittest import TestCase

from sme_credits.response_data_types.list.lists import SMEList
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.steps.list.step_get_list import step_get_list
from sme_credits.tests.steps.list.step_get_lists import step_get_lists
from sme_credits.tests.steps.list.step_post_list import step_post_list


class DemoTestCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.list = SMEList(
            data={
                "list_id": "001",
                "name": "birinchi",
                "user_employee": "Boxodir",
                "active": True
            }
        )

    # def test_post_list(self):
    #     step_post_list(self.context)
    #
    def test_get_lists(self):
        step_get_lists(self.context)

    def test_get_list(self):
        step_get_list(self.context)
