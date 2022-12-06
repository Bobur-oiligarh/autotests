from sme_make_decision_making.requests.сriterion.delete_criterions import DeleteCriterion


def delete_criterion(context):
    response = DeleteCriterion(context).response()
    response.check_status("Success").check_data_is_null()

