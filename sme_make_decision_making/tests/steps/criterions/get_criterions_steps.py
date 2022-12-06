from sme_make_decision_making.requests.сriterion.get_criterions import GetCriterions, GetCriterion


def get_criterions(context):
    response = GetCriterions().response()
    response.check_success(context).data.set_data_to(context)

def get_criterion(context):
    response = GetCriterion(context.criterion_id).response()
    response.check_success(context).data.set_data_to(context)
