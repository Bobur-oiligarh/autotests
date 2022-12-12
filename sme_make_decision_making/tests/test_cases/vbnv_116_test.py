from unittest import TestCase

import allure
from parameterized import parameterized

from sme_make_decision_making.response_data_types.lists import SMEList
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_116_scenario import vbnv_116_scenario
from utils.file_reader import FileReader


def parameters_creator():
    parameters = []
    table = FileReader().get("vbnv_116.csv")
    for line in table:
        context = SMEContext()
        context.list = SMEList(line)
        parameters.append([context])

    return parameters


class VBNV116TestCase(TestCase):
    @parameterized.expand(parameters_creator())
    @allure.tag("VBNV-116")
    @allure.title("УС.СПР, справочники (List)")
    def test_vbnv_116_scenario(self, context):
        vbnv_116_scenario(context)


