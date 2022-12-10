import allure

from sme_make_decision_making.requests.сriterion.patch_criterions import PatchCriterion


@allure.step("Запрос изменения criterion")
def patch_criterion(context):
    response = PatchCriterion(context).response()
    response.check_status("Success").check_data_is_null()
