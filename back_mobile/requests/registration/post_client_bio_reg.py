import base64

from back_mobile.response_data_types.registration.access_refresh_tokens import StoreAccRefTokens
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


# class PostBioRegistration(TestRequest):
#     def __init__(self, context):
#         super().__init__(
#             URLProvider.url("back_mobile", "api/v1/mobile/client-bio-registration"),
#             "post",
#             data_type=StoreAccRefTokens
#         )
#         self.birth_date = context.user.birth_date
#         self.doc_number = context.user.doc_number
#         self.doc_series = context.user.doc_series
#         self.doc_type = context.user.doc_type
#         self.photo = {"front": "" + base64.b64encode(context.photo)}

