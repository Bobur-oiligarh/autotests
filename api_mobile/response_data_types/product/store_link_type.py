import allure

from utils.api_utils.response_data_base import BaseTypeParent
from api_mobile.test_data.client import Client


class StoreLinkType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.link: str = data["link"]
        self.count_order: int = data["count_order"]

    def set_data_to(self, obj):
        self.set_link_to_client(obj)

    @allure.step("Установить ссылку на HamkorStore клиенту")
    def set_link_to_client(self, client: Client):
        client.webview_link = self

    def check(self, client, **kwargs):
        self.link_not_empty()
        self.count_order_not_null()

    @allure.step("count_order не пустой")
    def count_order_not_null(self):
        self._tc.assertNotEqual(self.count_order, None,
                                f"cont_order ({self.count_order}) пустой" + self.__str__())

    @allure.step("link не пустой")
    def link_not_empty(self):
        self._tc.assertNotEqual(self.link, "",
                                f"link ({self.link}) пустой" + self.__str__())
