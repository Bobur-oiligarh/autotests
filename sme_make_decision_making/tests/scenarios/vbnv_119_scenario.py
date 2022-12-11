import allure

from sme_make_decision_making.tests.steps.strategy.step_delete_strategy import step_delete_strategy
from sme_make_decision_making.tests.steps.strategy.step_get_strategies import step_get_strategies
from sme_make_decision_making.tests.steps.strategy.step_patch_strategy import step_patch_strategy
from sme_make_decision_making.tests.steps.strategy.step_post_strategy import step_post_strategy


@allure.step("Сценарий проверки работы классов на запросы POST, GET, GET ALL, PATCH, DELETE")
def vbnv_119_scenario(context):
    # Запрос всех объектов стратегии
    step_get_strategies(context)

    # Запрос добавление новой стратегии, проверка добавления
    step_post_strategy(context)
    step_get_strategies(context)
    context.strategies.exist(param_name="id", param_value=context.strategy.id)

    # Изменнение значения параметра у стратегии, проверка изменения
    context.strategy.change_param_value(param_name="product_id", param_value="11111")
    step_patch_strategy(context)
    step_get_strategies(context)
    context.strategy.check_objects_similarity(
        context.strategies.get_strategy_by_param(param_name="id", param_value=context.strategy.id)
    )

    # Запрос на удаления стратегии, проверка удаления
    step_delete_strategy(context)
    step_get_strategies(context)
    context.strategies.not_exist(param_name="id", param_value=context.strategy.id)


