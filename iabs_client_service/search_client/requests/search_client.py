from utils.api_utils.test_request import TestRequest
from utils.api_utils.url_provider import URLProvider


class IABSClientById(TestRequest):
    """Makes request to get IABS client by his ID."""

    def __init__(self, client_uid: str):
        super().__init__(
            URLProvider().url("iabs_clients_service", "search_clients", "search_clients_by_id",
                              f'?client_uid={client_uid}')
        )
