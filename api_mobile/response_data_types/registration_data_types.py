from api_mobile.response_data_types.base import BaseType


class SignId(BaseType):
    def __init__(self, data: dict):
        self.sign_id = data["sign_id"]


class ConfirmMethod(SignId):
    def __init__(self, data: dict):
        super().__init__(data)
        self.confirm_method = data["confirm_method"]


class AccRefTokens(BaseType):
    def __init__(self, data: dict):
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]


class Offer(BaseType):
    def __init__(self, data: dict):
        self.text = data["text"]
        self.is_short_title = data["is_short_title"]
        self.short_text = data["short_text"]


class AgreeResult(BaseType):
    def __init__(self, data: dict):
        self.result = data["result"]


class StoreAccRefTokens(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data["url"]


