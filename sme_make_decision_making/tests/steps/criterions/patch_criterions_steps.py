from sme_make_decision_making.requests.сriterion.patch_criterions import PatchCriterion


def patch_criterion(context):
    response = PatchCriterion(context).response()
    response.check_status("Success").check_data_is_null()
