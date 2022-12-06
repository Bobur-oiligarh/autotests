from sme_make_decision_making.tests.steps.criterions.get_criterions_steps import get_criterions, get_criterion


def demo_criterion_scenario(context):
    get_criterions(context)
    context.criterion_id = context.criterions.criterions[0].id
    get_criterion(context)