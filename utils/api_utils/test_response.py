from unittest import TestCase

import allure
from requests import Response
import json

from utils.methods import obj_to_string


class TestResponse:

    def __init__(self, response: Response, data_type: type, require_err_note: bool = True):
        self._tc = TestCase()
        resp_dict = json.loads(response.text)
        self._require_error_note = require_err_note

        self._raw_response_text = response.text
        self.data: data_type = None
        self.status = resp_dict["status"]
        self.error_code = resp_dict["error_code"]
        self.error_note = None if not require_err_note else resp_dict["error_note"]
        self._set_data(resp_dict["data"], data_type)

    def _set_data(self, data, data_type: type):
        """
        Десериализует параметр data в объект класса data_type
        :param data: содержимое параметра data ответа
        :param data_type: имя класса в который нужно десериализовать data
        :return: None
        """
        if data_type and data is not None:
            self.data = data_type(data)
        else:
            self.data = data

    @allure.step("Проверка ответа - положительный результат")
    def check_success(self, context, **kwargs):
        self.check_status("Success") \
            .check_error_code(0) \
            .check_error_note("") \
            .check_data_not_null() \
            .check_data_parameters(context)
        return self

    @allure.step("Проверка ответа - отрицательный результат")
    def check_failure(self, status, error_code, error_note):
        self.check_status(status) \
            .check_error_code(error_code) \
            .check_error_note(error_note) \
            .check_data_is_null()
        return self

    @allure.step("Проверка статуса ответа")
    def check_status(self, expected_status: str):
        self._tc.assertEqual(self.status, expected_status,
                             f"Статус ответа ({self.status}) не соответствует "
                             f"ожидаемому ({expected_status})" + self._raw_response_text)
        return self

    @allure.step("Проверка error_code")
    def check_error_code(self, expected_error_code: int):
        self._tc.assertEqual(self.error_code, expected_error_code,
                             f"error_code ({self.error_code}) не соответствует "
                             f"ожидаемому ({expected_error_code})" + self._raw_response_text)
        return self

    @allure.step("Проверка error_note")
    def check_error_note(self, expected_error_note: str):
        if self._require_error_note:
            self._tc.assertEqual(self.error_note, expected_error_note,
                                 f"error_note ({self.error_note}) не соответствует "
                                 f"ожидаемому ({expected_error_note})" + self._raw_response_text)
        return self

    @allure.step("Проверка data ответа не null")
    def check_data_not_null(self):
        self._tc.assertIsNotNone(self.data,
                                 f"data ответа является null" + self._raw_response_text)
        return self

    @allure.step("Проверка data ответа null")
    def check_data_is_null(self):
        self._tc.assertIsNone(self.data,
                              f"data ответа не является null" + self._raw_response_text)
        return self

    @allure.step("Проверка параметров данных ответа")
    def check_data_parameters(self, context, **kwargs):
        self.data.check(context, **kwargs)
        return self

    def __str__(self):
        return obj_to_string(self)
