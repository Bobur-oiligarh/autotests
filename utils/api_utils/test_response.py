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

    def _set_data(self, data, data_type: type):
        try:
            if data_type:
                self.data = data_type(data)
            else:
                self.data = data
        except:
            if data is None:
                assert f"data is None: {data}"

    def __str__(self):
        return obj_to_string(self)
