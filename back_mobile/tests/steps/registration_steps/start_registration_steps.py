import allure

from back_mobile.requests.registration.post_start_reg import PostStartReg


@allure.step("Начало регистрации start_registration")
def step_start_reg_success(context):
    response = PostStartReg(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Начало регистрации start_registration")
def step_start_reg_unsupported_version(context):
    context.app_version = "1.0.0"
    response = PostStartReg(context).response()
    response.check_failure("Failure", 1027,
                           "Эта версия приложения теперь не поддерживается.Обновите приложение")


@allure.step("Начало регистрации start_registration")
def step_start_reg_empty_phone(context):
    context.user.phone_number = ""
    response = PostStartReg(context).response()
    response.check_failure("Failure", -70,
                           "Key: 'reqStartReg.Phone' Error:Field validation for 'Phone' failed on the 'required' tag")


@allure.step("Начало регистрации start_registration")
def step_start_reg_empty_phone_type(context):
    context.device.phone_type = ""
    response = PostStartReg(context).response()
    response.check_failure("Failure", -70,
                           "Key: 'reqStartReg.PhoneType' "
                           "Error:Field validation for 'PhoneType' failed on the 'required' tag")
