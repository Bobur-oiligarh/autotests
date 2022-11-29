import allure

from onboarding_physical.requests.internal.post_private_contact import PostPrivateContact


@allure.step("Запрашиваем контакт и проверяем ответ запроса ")
def step_private_contact(context):
    response = PostPrivateContact(context).response()
    response.check_success(context=context).data.set_data_to(context)