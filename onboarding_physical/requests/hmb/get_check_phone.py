from onboarding_physical.response_data_types.hmb.check_phone import CheckPhone
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetCheckPhone(TestRequest):

    def __init__(self):
        super().__init__(
            URLProvider().url("onboarding_physical", "check-phone"),
            method="get",
            data_type=CheckPhone,
            params={'phone': '998941775859', 'phone_type': '0'}
        )
