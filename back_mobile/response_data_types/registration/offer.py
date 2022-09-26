import allure

from utils.api_utils.response_data_base import BaseType

__all__ = [
    "Offer",
    "AgreeOfferResult"
]


class Offer(BaseType):
    def __init__(self, data: dict):
        super().__init__()
        self.text = data["text"]
        self.is_short_title = data["is_short_title"]
        self.short_text = data["short_text"]

    def check(self, client, **kwargs):
        self.assert_not_empty("text")
        self.true_text_language(client)

    @allure.step("язык текста совпадает с ожидаемым")
    def true_text_language(self, client):
        # подумать над проверкой языка текста
        pass


class AgreeOfferResult(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.result = data["result"]

    def check(self, client, **kwargs):
        self.result_signing_offer("Success" if client.offer_sign_action == "accept" else kwargs["expected_sign_result"])

    @allure.step("проверка результата подписания оферты")
    def result_signing_offer(self, expected_result):
        self._tc.assertEqual(self.result, expected_result,
                             f"результат подписания оферты ({self.result}) "
                             f"отличается от ожидаемого ({expected_result})" + self.__str__())
