import allure
from requests import Response
import json

from utils.methods import obj_to_string


class TestResponse:

    def __init__(self, response: Response, data_type: type):
        resp_dict = json.loads(response.text)

        self.data: data_type = None

        self.status = resp_dict["status"]
        self.error_code = resp_dict["error_code"]
        self.error_note = resp_dict["error_note"]
        self._set_data(resp_dict["data"], data_type)

    @allure.step("Проверка ответа")
    def check_response(self, client, status, error_code, error_note, **kwargs):
        self.check_status(status)
        self.check_error_code(error_code)
        self.check_error_note(error_note)
        self.check_data(client, **kwargs)

    @allure.step("Статус ответа соответствует ожидаемому")
    def check_status(self, status):
        assert self.status == status, f"Статус ответа ({self.status}) не соответствует ожидаемому ({status})"

    @allure.step("Error_code ответа соответствует ожидаемому")
    def check_error_code(self, error_code):
        assert self.error_code == error_code, f"Error_code ответа ({self.error_code}) не соответствует ожидаемому ({error_code}) "

    @allure.step("Error_note ответа соответствует ожидаемому")
    def check_error_note(self, error_note):
        assert self.error_note == error_note, f"Error_note ответа ({self.error_note}) не соответствует ожидаемому ({error_note}) "

    @allure.step("Проверка параметров ответа")
    def check_data(self, client, **kwargs):
        self.data.check(client, **kwargs)

    def _set_data(self, data, data_type: type):
        try:
            if data_type:
                self.data = data_type(data)
            else:
                self.data = data
        except:
            print("class: TestResponse; method: set_data;")
            if data is None:
                assert f"data is None: {data}"

    def __str__(self):
        return obj_to_string(self)
