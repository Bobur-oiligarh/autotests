import allure

from sme_make_decision_making.requests.сriterion.delete_criterions import DeleteCriterion


@allure.step("Запрос удаления criterion")
def delete_criterion(context):
    response = DeleteCriterion(context).response()
    response.check_status("Success").check_data_is_null()
