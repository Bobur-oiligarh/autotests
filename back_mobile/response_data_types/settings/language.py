import allure

from utils.api_utils.response_data_base import BaseType

__all__ = [
    "ChangeLangResult"
]


class ChangeLangResult(BaseType):

    def __init__(self, result: str):
        super().__init__()
        self.result = result

    def check(self, client, **kwargs):
        self.assert_not_empty("result")
        self.assert_equal("result",
                          "Успешно установлен" if "expected_result" not in kwargs.keys() else kwargs["expected_result"])
