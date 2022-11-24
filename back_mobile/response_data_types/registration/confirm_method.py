import allure

from back_mobile.response_data_types.registration.sign_id import SignId

__all__ = [
    "ConfirmMethod"
]


class ConfirmMethod(SignId):
    def __init__(self, data: dict):
        super().__init__(data)
        self.confirm_method = data["confirm_method"]

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        self.assert_not_empty_str("confirm_method")
        self.assert_equal("confirm_method", client.confirm_method)

    def set_data_to(self, obj):
        super().set_data_to(obj)
        self.set_confirm_method(obj)

    @allure.step("Установить confirm_method")
    def set_confirm_method(self, client):
        client.confirm_method = self.confirm_method
