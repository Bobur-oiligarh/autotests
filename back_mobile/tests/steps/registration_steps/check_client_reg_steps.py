import allure

from back_mobile.requests.registration.post_check_client_reg import PostCheckClientReg


@allure.step("Добавление карты check_client_registration")
def step_check_client_reg(context):
    response = PostCheckClientReg(context).response()
    response.check_success(context).data.set_data_to(context)
