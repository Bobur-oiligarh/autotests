from utils.api_utils.response_data_base import BaseType


class ChangeLang(BaseType):

    def __init__(self, result: str):
        super().__init__()
        self.result = result

    def check(self, context, **kwargs):
        self.assert_not_empty_str("result")
        self.assert_equal_param("result",
                          "Успешно установлен" if "expected_result" not in kwargs.keys() else kwargs["expected_result"])
