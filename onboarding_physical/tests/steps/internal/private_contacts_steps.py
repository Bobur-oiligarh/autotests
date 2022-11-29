import allure

from onboarding_physical.requests.internal.get_private_contacts import GetPrivateContacts


@allure.step("Запрос на получения контактов по contactID")
def step_private_contacts(context):
    response = GetPrivateContacts(context).response()
    response.check_success(context).data.set_data_to(context)
