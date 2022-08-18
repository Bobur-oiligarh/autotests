from api_mobile.response_data_types.registration_data_types import Offer, AgreeOfferResult
from utils.api_utils.test_request import TestRequest
from api_mobile.test_data.client import Client
from api_mobile.test_data.providers import URLProvider


class GetOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "get_offer"),
            data_type=Offer,
            headers=client.auth_token()
        )


class AgreeOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "agree_offer"),
            data_type=AgreeOfferResult,
            headers=client.auth_token()
        )
        self.action = client.action

