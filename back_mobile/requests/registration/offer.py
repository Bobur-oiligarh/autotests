from back_mobile.response_data_types.registration.offer import Offer, AgreeOfferResult
from utils.api_utils.test_request import TestRequest
from back_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider


class GetOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "registration", "get_offer"),
            data_type=Offer,
            headers=client.auth_token()
        )


class AgreeOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "registration", "agree_offer"),
            data_type=AgreeOfferResult,
            headers=client.auth_token()
        )
        self.action = client.offer_sign_action
