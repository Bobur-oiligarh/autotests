import allure

from onboarding_physical.requests.internal.private_prospects import PrivateProspectsRequest


@allure.step("Поиск или создание проспекта по iabdClientID и номеру телефона")
def step_private_prospects(context):
    response = PrivateProspectsRequest(context).response()
    response.check_success(context).data.set_data_to(context)
