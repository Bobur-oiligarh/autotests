from utils.api_utils.response_data_base import BaseType
import allure


class SignId(BaseType):

    def __init__(self, data: dict):
        self.sign_id = data["sign_id"]

    def check(self, client, **kwargs):
        self.sign_id_not_empty()

    @allure.step("Sign_id не пустой")
    def sign_id_not_empty(self):
        assert self.sign_id != "", f"Sign_id ответа пустой"


class AccRefTokens(BaseType):

    def __init__(self, data: dict):
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def check(self, client, **kwargs):
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

    def check(self, client, **kwargs):
        self.text_not_empty()
        self.true_text_language(client)

    @allure.step("Текст не пустой")
    def text_not_empty(self):
        assert len(self.text) > 0, f"Текст в ответе пустой"

    @allure.step("Язык текста совпадает с ожидаемым")
    def true_text_language(self, client):
        # подумать над проверкой языка текста
        pass


class AgreeOfferResult(BaseType):

    def __init__(self, data: dict):
        self.result = data["result"]

    def check(self, client, **kwargs):
        self.result_is_success(
            kwargs["result"] if "result" in kwargs.keys() else "Success"
        )

    @allure.step("Проверка результата подписания оферты")
    def result_is_success(self, expected_result):
        assert self.result == expected_result, f"" \
                                               f"Результат подписания оферты ({self.result}) " \
                                               f"отличается от ожидаемого ({expected_result})"


class ConfirmMethod(SignId):
    def __init__(self, data: dict):
        super().__init__(data)
        self.confirm_method = data["confirm_method"]

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        self.check_confirm_method(
            kwargs["confirm_method"] if "confirm_method" in kwargs.keys() else "BIO"
        )

    @allure.step("Проверка confirm_method")
    def check_confirm_method(self, expected_confirm_method):
        self.confirm_method_not_empty()
        self.confirm_method_not_empty()

    @allure.step("confirm_method не пустой")
    def confirm_method_not_empty(self):
        assert len(self.confirm_method) > 0, f"confirm_method пустой"

    @allure.step("confirm_method совпадает с ожидаемым")
    def confirm_method_is_true(self, expected_confirm_method):
        assert self.confirm_method == expected_confirm_method, f"confirm_method ответа ({self.confirm_method}) не " \
                                                               f"совпадает с ожидаемым ({expected_confirm_method})"


class StoreAccRefTokens(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data["url"]
