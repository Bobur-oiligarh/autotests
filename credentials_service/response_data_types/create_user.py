import allure

from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens


class CreateUser(AccRefTokens):

    def __init__(self, data: dict):
        super().__init__(data)
        self.user_id = data["user_id"]

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    @allure.step("Установить данные в контекст")
    def set_data_to_context(self, context):
        context.refresh_token = self.refresh_token
        context.access_token = self.access_token
        context.user_id = self.user_id

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_str("user_id")
