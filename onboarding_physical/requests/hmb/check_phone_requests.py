from onboarding_physical.response_data_types.hmb.check_phone_response_data_types import CheckPhoneResponseDatatype
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class CheckPhoneRequest(TestRequest):

    def __init__(self):
        super().__init__(
            URLProvider().url("onboarding_physical", "check-phone"),
            method="get",
            data_type=CheckPhoneResponseDatatype,
            params={'phone': '998941775859', 'phone_type': '0'}
        )
