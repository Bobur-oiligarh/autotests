import allure

from api_mobile.response_data_types.response_data_base import BaseType


class Offer(BaseType):
    def __init__(self, data: dict):
        super().__init__()
        self.text = data["text"]
        self.is_short_title = data["is_short_title"]
        self.short_text = data["short_text"]

    def check(self, client, **kwargs):
        self.text_not_empty()
        self.true_text_language(client)

    @allure.step("текст не пустой")
    def text_not_empty(self):
        assert len(self.text) > 0, f"текст в ответе пустой"

    @allure.step("язык текста совпадает с ожидаемым")
    def true_text_language(self, client):
        # подумать над проверкой языка текста
        pass


class AgreeOfferResult(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.result = data["result"]

    def check(self, client, **kwargs):
        self.result_is_success(
            kwargs["result"] if "result" in kwargs.keys() else "Success"
        )

    @allure.step("проверка результата подписания оферты")
    def result_is_success(self, expected_result):
        assert self.result == expected_result, \
            f"результат подписания оферты ({self.result}) " \
            f"отличается от ожидаемого ({expected_result})"