from back_mobile.response_data_types.registration.offer import Offer, AgreeOfferResult
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetOffer(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/registration-offer"),
            "get",
            data_type=Offer,
            headers=context.auth_token()
        )


class AgreeOffer(TestRequest):
    def __init__(self, context):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/registration-offer"),
            "put",
            data_type=AgreeOfferResult,
            headers=context.auth_token()
        )
        self.action = context.offer_sign_action
