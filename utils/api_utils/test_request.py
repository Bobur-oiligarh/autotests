import allure
import requests
import json
from abc import ABC

from utils.api_utils.test_response import TestResponse

methods = {
    "post": requests.post,
    "get": requests.get,
    "put": requests.put,
    "delete": requests.delete,
    "patch": requests.patch}


class RequestBase:

    def __init__(self,
                 url: dict,
                 data_type: type = None,
                 data: str = None,
                 headers: dict = None,
                 cookies: dict = None):

        self._response = None
        self._data_type = data_type
        self._method = url["method"]
        self._url = url["url"]
        self._data = data
        self._headers = headers
        self._cookies = cookies

    def _run(self):
        response = methods[self._method](
            url=self._url,
            data=self._get_data(),
            headers=self._headers,
            cookies=self._cookies
        )
        print(self.__dict__)
        self._response = TestResponse(response, self._data_type)

    def response(self, refresh: bool = False) -> TestResponse:
        if refresh or self._response is None:
            self._run()
        return self._response

    def status(self):
        return self.response().status

    def error_code(self):
        return self.response().error_code

    def error_note(self):
        return self.response().error_note

    def data(self):
        return self.response().data

    def _get_data(self) -> str:
        data = {}
        for key in self.__dict__:
            if not key.startswith("_"):
                data[key] = getattr(self, key)
        return json.dumps(data)


class TestRequest(RequestBase, ABC):

    @allure.step("Отправляем запрос, получаем ответ")
    def _run(self):
        super()._run()
