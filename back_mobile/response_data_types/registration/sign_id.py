import allure

from utils.api_utils.response_data_base import BaseTypeParent


class SignId(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.sign_id = data["sign_id"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("sign_id")

    def set_data_to(self, obj):
        self.set_sign_id(obj)

    @allure.step("Установить sign_id")
    def set_sign_id(self, context):
        context.sign_id = self.sign_id
        return self
