from unittest import TestCase

from sme_credits.response_data_types.list.lists import SMEList
from sme_credits.test_data.sme_context import SMEContext
from sme_credits.tests.steps.list.step_delete_list import step_delete_list
from sme_credits.tests.steps.list.step_get_list import step_get_list
from sme_credits.tests.steps.list.step_get_list_accounts import step_get_list_accounts
from sme_credits.tests.steps.list.step_get_lists import step_get_lists
from sme_credits.tests.steps.list.step_patch_list import step_patch_list
from sme_credits.tests.steps.list.step_post_list import step_post_list


class DemoTestCase(TestCase):

    def setUp(self) -> None:
        self.context = SMEContext()
        self.context.list = SMEList(
            data={
                "list_id": "AL009",
                "name": "ikkinchi",
                "user_employee": "Boxodir",
                "active": False
            }
        )

    # def test_post_list(self):
    #     step_post_list(self.context)
    #
    # def test_get_lists(self):
    #     step_get_lists(self.context)
    #
    # def test_get_list(self):
    #     step_get_list(self.context)

    # def test_patch_list(self):
    #     step_patch_list(self.context)

    # def test_delete_list(self):
    #     step_delete_list(self.context)

    # def test_get_list_accounts(self):
    #     step_get_list_accounts(self.context)

