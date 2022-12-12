import allure

from sme_make_decision_making.tests.steps.list.step_delete_list import step_delete_list
from sme_make_decision_making.tests.steps.list.step_get_list import step_get_lists, step_get_list_assert_equal
from sme_make_decision_making.tests.steps.list.step_patch_list import step_patch_list
from sme_make_decision_making.tests.steps.list.step_post_list import step_post_list


@allure.step("Сценарий проверки работы end_point List")
def vbnv_116_scenario(context):
    # Запрос всех объектов list
    step_get_lists(context)
    context.lists.assert_obj_not_exist("lists", "list_id", context.list.list_id)

    # Запрос добавление нового list, проверка добавления
    step_post_list(context)
    step_get_lists(context)
    context.lists.assert_obj_exist("lists", param_name="list_id", param_value=context.list.list_id)

    # Изменнение значения параметра у list, проверка изменения
    context.list.active = True
    step_patch_list(context)
    step_get_lists(context)
    context.list.assert_equal(
        obj=context.lists.get_obj_by_param("lists", param_name="list_id", param_value=context.list.list_id)
        )

    # Проверка запроса GET list by list_id
    step_get_list_assert_equal(context)

    # Запрос на удаления list, проверка удаления
    step_delete_list(context)
    step_get_lists(context)
    context.lists.assert_obj_not_exist("lists", param_name="list_id", param_value=context.list.list_id)
