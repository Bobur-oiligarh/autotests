import allure

from sme_make_decision_making.requests.сriterion.get_criterions import GetCriterions, GetCriterion


@allure.step("Запрос получения всех criterions")
def get_criterions(context):
    response = GetCriterions().response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос criterion по его id")
def get_criterion(context):
    response = GetCriterion(context.criterion.id).response()
    response.check_success(context)
    return response.data

@allure.step("Запрос criterion и его сопоставление")
def get_criterion_check_equal(context):
    criterion = get_criterion(context)
    context.criterion.assert_equal(criterion)

