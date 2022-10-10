import allure

from limit_module.requests.p2p_all_oper_limit_request import P2PAllOperationsLimitRequest


@allure.step("Запрашиваем лимит по p2p операции и проверяем")
def step_p2p_all_limit(context):
    response = P2PAllOperationsLimitRequest(context).response()
    response.check_success(context).data.set_data_to(context)
