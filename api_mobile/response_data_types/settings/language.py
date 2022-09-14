import allure

from utils.api_utils.response_data_base import BaseType


class ChangeLangResult(BaseType):

    def __init__(self, result: str):
        super().__init__()
        self.result = result

    def check(self, client, **kwargs):
        self.result_not_empty()
        self.result_is_true(
            "Успешно установлен" if "expected_result" not in kwargs.keys() else kwargs["expected_result"]
        )

    @allure.step("result не пустой")
    def result_not_empty(self):
        self._tc.assertIsNotNone(self.result,
                                 f"result пустой")

    @allure.step("result соответствует ожидаемому")
    def result_is_true(self, expected_result):
        self._tc.assertEqual(self.result, expected_result,
                             f"result ({self.result}) не соответствует "
                             f"ожидаемому ({expected_result})" + self.__str__())
