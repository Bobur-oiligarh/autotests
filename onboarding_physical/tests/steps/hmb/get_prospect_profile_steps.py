import allure

from onboarding_physical.requests.hmb.get_prospect_profile_requests import ProspectProfileRequest


@allure.step('Делаем запрос на проспект профайл и проверяем ответ')
def step_get_prospect_profile(context):
    response = ProspectProfileRequest(context).response()
    response.check_success(context).data.set_data_to(context)
