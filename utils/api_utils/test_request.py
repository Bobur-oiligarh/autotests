import allure
import requests
import json
from abc import ABC

from utils.api_utils.response_data_base import BaseType
from utils.api_utils.test_response import TestResponse

# методы библиотеки requests
methods = {
    "post": requests.post,
    "get": requests.get,
    "put": requests.put,
    "delete": requests.delete,
    "patch": requests.patch}


class RequestBase:

    def __init__(self,
                 url: str,
                 method: str,
                 data_type: type = None,
                 data: dict = None,
                 headers: dict = None,
                 cookies: dict = None,
                 parameters_in_list: bool = False,
                 name_of_list: str = None,
                 params: dict = None):

        """
        :param url: {"method": "метод запроса", "url": "url запроса"}
        :param data_type: тип данных ответа
        :param data: тело запроса
        :param headers: хедеры запроса
        :param cookies: куки запроса
        :param parameters_in_list: если в теле запроса json список, то true
        :param name_of_list: имя переменной с json списком
        :param params: параметры запроса
        """

        self._response = None
        self._data_type = data_type
        self._url = url
        self._method = method
        self._data = data
        self._headers = headers
        self._cookies = cookies
        self._params = params

        self._parameters_in_list: bool = parameters_in_list  #
        self._name_of_list: str = name_of_list  #

    def response(self, refresh: bool = False) -> TestResponse:
        """
        Возвращает ответ на запрос
        :param refresh: true если нужно отправить запрос повторно
        :return: TestResponse объект ответа
        """
        if refresh or self._response is None:
            self._run()
        return self._response

    def _run(self):
        """
        Отправляет запрос, создает и сохраняет объект ответа
        :return:
        """
        response = methods[self._method](
            url=self._url,
            data=self._get_data(),
            headers=self._headers,
            cookies=self._cookies,
            params=self._params
        )
        self._response = TestResponse(response, self._data_type)

    def _get_data(self) -> json:
        """
        Сериализует поля без префикса "_" в параметры тела запроса,
        в качестве имени параметра будет использовано имя переменной
        :return: сериализованный в json строку объект запроса
        """
        if not self._parameters_in_list:
            data = {}
            for key in self.__dict__:
                if not key.startswith("_"):
                    if isinstance(getattr(self, key), BaseType):
                        data[key] = getattr(self, key).to_dict()
                    else:
                        data[key] = getattr(self, key)
        else:
            data = self.__dict__[self._name_of_list]
        return json.dumps(data)

    def data(self):
        return self._data


class TestRequest(RequestBase, ABC):

    def _get_data(self) -> json:
        # with allure.step(json.dumps(self.data())):
        #     pass
        # if self.data():
        #     return json.dumps(self.data())
        return super()._get_data()

    @allure.step("Отправляем запрос, получаем ответ")
    def _run(self):
        super()._run()
