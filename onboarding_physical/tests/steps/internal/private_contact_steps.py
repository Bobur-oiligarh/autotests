import allure

from onboarding_physical.requests.internal.private_contact_requests import PrivateContactRequest


@allure.step("Запрашиваем контакт и проверяем ответ запроса ")
def step_private_contact(context):
    response = PrivateContactRequest(context).response()
    response.check_success(context=context).data.set_data_to(context)