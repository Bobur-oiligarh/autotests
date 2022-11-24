import allure

from back_mobile.requests.registration.offer import AgreeOffer

__all__ = [
    "step_agree_offer"
]


@allure.step("Подтверждение оферты agree_offer")
def step_agree_offer(client):
    response = AgreeOffer(client).response()
    response.check_success(client)
