from sme_make_decision_making.tests.steps.criterions.delete_criterions_steps import delete_criterion
from sme_make_decision_making.tests.steps.criterions.get_criterions_steps import get_criterions, get_criterion_check_equal
from sme_make_decision_making.tests.steps.criterions.patch_criterions_steps import patch_criterion
from sme_make_decision_making.tests.steps.criterions.post_criterions_steps import post_criterion


def vbnv_118_scenario(context):
    # запрашиваем все criterions и проверяем на наличие в списке того, который собираемся создавать
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)

    # создаем новый и проверяем добавление
    post_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_exist("criterions", "id", context.criterion.id)

    # меняем добавленный criterion и проверяем его изменение
    context.criterion.name = "Наличие правого полужопия"
    patch_criterion(context)
    get_criterions(context)
    context.criterions.get_obj_by_param(
        "criterions", "id", context.criterion.id
    ).assert_equal(context.criterion)

    # запрашиваем criterion по id и проверяем его соответствие ожидаемому
    get_criterion_check_equal(context)

    # удаляем criterion и проверяем удаление
    delete_criterion(context)
    get_criterions(context)
    context.criterions.assert_obj_not_exist("criterions", "id", context.criterion.id)

