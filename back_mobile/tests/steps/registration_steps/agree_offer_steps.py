import allure

from back_mobile.requests.registration.get_put_offer import PutOffer


@allure.step("Подтверждение оферты agree_offer")
def step_agree_offer(context):
    response = PutOffer(context).response()
    response.check_success(context)
