import allure

from sme_make_decision_making.requests.сriterion.post_criterions import PostCriterion


@allure.step("Запрос создания нового criterion")
def post_criterion(context):
    response = PostCriterion(context).response()
    response.check_success(context).data.set_data_to(context)
