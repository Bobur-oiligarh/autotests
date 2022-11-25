import allure

from back_mobile.requests.registration.get_put_offer import GetOffer


@allure.step("Запрос оферты get_offer")
def step_get_offer(context):
    response = GetOffer(context).response()
    response.check_success(context)
