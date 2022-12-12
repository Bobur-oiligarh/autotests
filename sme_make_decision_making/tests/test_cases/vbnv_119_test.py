from unittest import TestCase

import allure
from parameterized import parameterized

from sme_make_decision_making.response_data_types.strategies import SMEStrategy
from sme_make_decision_making.test_data.sme_context import SMEContext
from sme_make_decision_making.tests.scenarios.vbnv_119_scenario import vbnv_119_scenario
from utils.file_reader import FileReader


def parameters_creator():
    parameters = []
    table = FileReader().get("vbnv_119.csv")
    for line in table:
        context = SMEContext()
        context.strategy = SMEStrategy(line)
        parameters.append([context])

    return parameters


class VBNV119TestCase(TestCase):

    @parameterized.expand(parameters_creator())
    @allure.tag("VBNV-119")
    @allure.title("УС.СПР, справочники (Strategy)")
    def test_strategy(self, context):
        vbnv_119_scenario(context)

#
# if __name__ == '__main__':
#     print(parameters_creator())
#     for context in parameters_creator():
#         print(context[0].strategy.__dict__)
#         print(type(context[0].strategy.product_id))