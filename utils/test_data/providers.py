from utils.api_utils.data.urls import urls
import os

from utils.patterns.singleton import Singleton
import pathlib


class URLProviderBase:

    def url(self, service_name, end_point) -> dict:
        url = {
            "url": self._environment(service_name) + urls[service_name][end_point]["path"],
            "method": urls[service_name][end_point]["method"]
        }
        return url

    @staticmethod
    def _environment(service_name) -> str:
        if len(urls[service_name]["environment"]["all"]) > 0:
            return urls[service_name]["environment"]["all"]
        return urls[service_name]["environments"][os.environ["ENVIRONMENT"]]


class URLProvider(URLProviderBase, metaclass=Singleton):
    pass


if __name__ == "__main__":
    print(URLProvider().url("registration", "finish_reg"))
