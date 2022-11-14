import allure

from card_service.response_data_types.cards_methods.crads import Cards
from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class GetCards(TestRequest):

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("card_service", "v2/cards"),
            method="get",
            data_type=Cards,
            params=self._params(context),
        )

    @staticmethod
    def _params(context):
        params = {}
        if context.phone:
            params["phone"] = context.phone
        if context.bins:
            params["bins"] = context.bins
        if context.iabs_client_id:
            params["iabs_client_id"] = context.iabs_client_id
        if context.prospect_id:
            params["prospect_id"] = context.prospect_id
        return params
