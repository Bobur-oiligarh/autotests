import allure

from onboarding_physical.requests.internal.private_contacts_requests import PrivateContactsRequest


@allure.step("Запрос на получения контактов по contactID")
def step_private_contacts(context):
    response = PrivateContactsRequest(context).response()
    response.check_success(context).data.set_data_to(context)
