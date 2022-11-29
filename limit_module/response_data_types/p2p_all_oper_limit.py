from limit_module.test_data.limit_module_context import LimitModuleContext
from utils.api_utils.response_data_base import BaseTypeParent, BaseType
import allure


class Limits(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.limits: list = self.deserialize_to_list_of(Limit, data)

    def check(self, context, **kwargs):
        self.check_list_of("limits", context, **kwargs)

    @allure.step("Устанавливаем лист лимитов к контексту")
    def set_data_to(self, obj: LimitModuleContext):
        self._set_data_to_product(obj)

    def _set_data_to_product(self, obj: LimitModuleContext):
        obj.limits = self


class Limit(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.type = data["Type"]
        self.value = data["Value"]

    def check(self, context, **kwargs):
        self.assert_not_empty_str("type")
        self.assert_not_empty_int("value")
