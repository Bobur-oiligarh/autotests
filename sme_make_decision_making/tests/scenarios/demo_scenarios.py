from sme_make_decision_making.tests.steps.criterions.delete_criterions_steps import delete_criterion
from sme_make_decision_making.tests.steps.criterions.get_criterions_steps import get_criterions, get_criterion
from sme_make_decision_making.tests.steps.criterions.patch_criterions_steps import patch_criterion
from sme_make_decision_making.tests.steps.criterions.post_criterions_steps import post_criterion


def demo_criterion_scenario(context):
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)
    post_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_exist("criterions", "id", context.criterion.id)
    context.criterion.name = "Наличие правого полужопия"
    patch_criterion(context)
    get_criterions(context)
    context.criterions.get_obj_by_param("criterions", "id", context.criterion.id).assert_equal(context.criterion)
    delete_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)

