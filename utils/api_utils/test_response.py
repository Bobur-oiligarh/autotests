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

    def check(self, status: str = "Success", error_code: int = 0, error_note: str = ""):
        self.check_status(status)
        self.check_error_code(error_code)
        self.check_error_note(error_note)

    def check_status(self, status):
        assert self.status == status, f"Response status ({self.status}) not as expected ({status})"

    def check_error_code(self, error_code):
        assert self.error_code == error_code, f"Response error code ({self.error_code}) not as expected ({error_code})"

    def check_error_note(self, error_note):
        assert self.error_note == error_note, f"Response error note ({self.error_note}) not as expected ({error_note})"

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
