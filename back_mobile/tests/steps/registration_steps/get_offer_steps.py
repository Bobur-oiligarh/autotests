import allure

from back_mobile.requests.registration import GetOffer
from utils.universal_steps.check_response import check_response

__all__ = [
    "step_get_offer"
]


@allure.step("Запрос оферты get_offer")
def step_get_offer(client):
    response = GetOffer(client).response()
    response.check_success(client)
