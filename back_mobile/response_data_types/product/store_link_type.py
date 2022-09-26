import allure

from utils.api_utils.response_data_base import BaseTypeParent
from back_mobile.test_data.client import Client

__all__ = [
    "StoreLinkType"
]


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
        self.assert_not_empty("link")
        self.assert_not_none("count_order")
