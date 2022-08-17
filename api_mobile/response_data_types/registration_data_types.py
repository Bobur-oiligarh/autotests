from utils.api_utils.response_data_base import BaseType
import allure


class SignId(BaseType):
    def __init__(self, data: dict):
        self.sign_id = data["sign_id"]

    def check(self, client):
        super().check(client)
        self.sign_id_not_empty()

    @allure.step("Sign_id не пустой")
    def sign_id_not_empty(self):
        assert self.sign_id != "", f"Sign_id ответа пустой"


class ConfirmMethod(SignId):
    def __init__(self, data: dict):
        super().__init__(data)
        self.confirm_method = data["confirm_method"]


class AccRefTokens(BaseType):
    def __init__(self, data: dict):
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def check(self, client):
        super().check(client)
        self.access_token_not_empty()
        self.refresh_token_not_empty()

    @allure.step("access_token не пустой")
    def access_token_not_empty(self):
        assert self.access_token != "", f"access_token ответа пустой"

    @allure.step("refresh_token не пустой")
    def refresh_token_not_empty(self):
        assert self.refresh_token != "", f"refresh_token ответа пустой"


class Offer(BaseType):
    def __init__(self, data: dict):
        self.text = data["text"]
        self.is_short_title = data["is_short_title"]
        self.short_text = data["short_text"]

    def check(self, client):
        self.text_not_empty(client)

    @allure.step("Текст не пустой")
    def text_not_empty(self):
        assert len(self.text) > 0, f"Текст в ответе пустой"

    @allure.step("Язык текста совпадает с ожидаемым")
    def true_text_language(self):
        pass



class AgreeOfferResult(BaseType):
    def __init__(self, data: dict):
        self.result = data["result"]


class StoreAccRefTokens(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data["url"]
