import base64

from back_mobile.response_data_types.registration import StoreAccRefTokens
from utils.api_utils.url_provider import URLProvider
from back_mobile.test_data.client import Client
from utils.api_utils.test_request import TestRequest


class BioRegistration(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider.url("back_mobile", "api/v1/mobile/client-bio-registration"),
            "post",
            data_type=StoreAccRefTokens
        )
        self.birth_date = client.user.birth_date
        self.doc_number = client.user.doc_number
        self.doc_series = client.user.doc_series
        self.doc_type = client.user.doc_type
        self.photo = {"front": "" + base64.b64encode(client.photo)}

