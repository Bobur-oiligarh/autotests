import allure

from onboarding_physical.requests.internal.post_private_prospects import PostPrivateProspects


@allure.step("Поиск или создание проспекта по iabdClientID и номеру телефона")
def step_private_prospects(context):
    response = PostPrivateProspects(context).response()
    response.check_success(context).data.set_data_to(context)
