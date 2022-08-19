import base64

from api_mobile.response_data_types.registration.registration_data_types import StoreAccRefTokens
from api_mobile.test_data.providers import URLProvider
from api_mobile.test_data.client import Client
from utils.api_utils.test_request import TestRequest


class BioIdentification(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider.url("registration", ""),
            data_type=StoreAccRefTokens
        )
        self.birth_date = client.user.birth_date
        self.doc_number = client.user.doc_number
        self.doc_series = client.user.doc_series
        self.doc_type = client.user.doc_type
        self.photo = {"front": "" + base64.b64encode(client.photo)}

