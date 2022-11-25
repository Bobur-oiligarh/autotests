import allure

from back_mobile.requests.registration.post_finish_reg import PostFinishRegistration


@allure.step("Подтверждение номера телефона finish_registration")
def step_finish_reg(context):
    response = PostFinishRegistration(context).response()
    response.check_success(context).data.set_data_to(context)
