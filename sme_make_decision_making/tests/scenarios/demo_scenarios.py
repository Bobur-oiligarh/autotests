from sme_make_decision_making.tests.steps.criterions.delete_criterions_steps import delete_criterion
from sme_make_decision_making.tests.steps.criterions.get_criterions_steps import get_criterions, get_criterion
from sme_make_decision_making.tests.steps.criterions.post_criterions_steps import post_criterion


def demo_criterion_scenario(context):
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)
    post_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_exist("criterions", "id", context.criterion.id)
    delete_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)

