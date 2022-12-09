from unittest import TestCase

import allure
from parameterized import parameterized

from sme_make_decision_making.response_data_types.criterions import SMECriterion
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_118_scenario import vbnv_118_scenario
from utils.file_reader import FileReader


def parameters_creator():
    parameters = []
    table = FileReader().get("vbnv_118.csv")
    for line in table:
        context = SMEContext()
        context.criterion = SMECriterion(line)
        parameters.append([context])

    return parameters


class VBNV118TestCase(TestCase):

    @parameterized.expand(parameters_creator())
    @allure.tag("VBNV-118")
    @allure.title("УС.СПР, справочники (Criterion)")
    def test_criterion(self, context):
        vbnv_118_scenario(context)
