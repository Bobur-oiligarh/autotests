import multiprocessing

from tests import services
from tests_runner import spawn_process
from utils.patterns.singleton import Singleton


class TestProcessProviderBase:
    _processes = {}

    def create_test_process(self, number, params: dict) -> str:
        process = multiprocessing.Process(
            target=spawn_process,
            args=(number, params,)
        )
        key = params.get("service")
        if key:
            self._processes[key] = process
        return key

    def start_process(self, key) -> bool:
        process = self._processes.get(key)
        if process:
            process.start()
            return True
        return False

    def kill_process(self, key) -> bool:
        process = self._processes.get(key)
        if process:
            process.kill()
            return True
        return False


class TestProcessProvider(TestProcessProviderBase, metaclass=Singleton):
    pass


if __name__ == "__main__":

    process_jobs = []
    for num, item in enumerate(services):
        process_key = TestProcessProvider().create_test_process(num, item)
        if process_key:
            TestProcessProvider().start_process(process_key)

    for p in process_jobs:
        p.join()
