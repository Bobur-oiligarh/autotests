from utils.settings import Settings
from _pytest.config import main as pt_main


def spawn_process(number, params: dict):
    print(f"Process number - {number}")
    tr = TestsRunner(params)
    tr.start_tests()


class TestsRunner:
    _command = []

    def __init__(self, params):
        self._params = params
        self.settings = Settings()
        self.settings.set_data(params)
        self.settings.set_tests(params)
        self.create_command()

    def create_command(self):
        self._set_tests()
        self._command.append("--alluredir")
        self._command.append("./results")
        self._command.append("-v")

    def _set_tests(self):
        if self._params.get("tests"):
            self._set_tests_from_params()
            return
        self._command.append(
            f"./{self._params.get('service')}/tests/test_cases/demo_test.py"
        )

    def _set_tests_from_params(self):
        for item in self._params.get("tests"):
            self._command.append(f"./{self._params.get('service')}/tests/test_cases/{item}_test.py")

    def start_tests(self):
        print(f"Start running tests of service <<{self._params.get('service')}>>")
        pt_main(self._command)
