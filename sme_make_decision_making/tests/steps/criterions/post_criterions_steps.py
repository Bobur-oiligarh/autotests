from sme_make_decision_making.requests.сriterion.post_criterions import PostCriterion


def post_criterion(context):
    response = PostCriterion(context).response()
    response.check_success(context).data.set_data_to(context)
