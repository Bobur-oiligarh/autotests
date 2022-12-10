import allure

from sme_make_decision_making.requests.сriterion.get_criterions import GetCriterions, GetCriterion


@allure.step("Запрос получения всех criterions")
def get_criterions(context):
    response = GetCriterions().response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос получения criterion по его id")
def get_criterion(context):
    response = GetCriterion(context.criterion_id).response()
    response.check_success(context).data.set_data_to(context)
