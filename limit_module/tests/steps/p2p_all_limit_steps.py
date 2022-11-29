import allure

from limit_module.requests.post_p2p_all_oper_limit import PostP2PAllOperationsLimit


@allure.step("Запрашиваем лимит по p2p операции и проверяем")
def step_p2p_all_limit(context):
    response = PostP2PAllOperationsLimit(context).response()
    response.check_success(context).data.set_data_to(context)
