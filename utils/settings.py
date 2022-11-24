import time
from unittest import TestLoader, TestResult

from utils.patterns.singleton import Singleton
import multiprocessing


class Settings(metaclass=Singleton):

    def __init__(self):
        self._ENV = None
        self._TEAM = None
        self._CON_TYPE = None
        self._SERVICE = None
        self._TESTS = None

    def set_data(self, data: dict):
        if None in self.__dict__.values():
            self._SERVICE = data.get("service")
            self._TEAM = data.get("team")
            self._CON_TYPE = data.get("con_type")
            self._ENV = data.get("env")
            self._TESTS = data.get("tests")
        return self

    def env(self):
        return self._ENV

    def team(self):
        return self._TEAM

    def con_type(self):
        return self._CON_TYPE

    def service(self):
        return self._SERVICE

    def tests(self):
        return self._TESTS


class Loader:
    def __init__(self):
        self._loader = TestLoader()
        self._s = Settings()

    def find_tests(self):
        suite = self._loader.discover(self._s.service(), pattern="*test.py")
        print(self._s.service())
        print(suite)
        print(suite.countTestCases())
        print()


def spawn_process(number, data):
    Settings().set_data(data)
    loader = Loader()
    loader.find_tests()
    time.sleep(number)
    print(f"\nThis is process: {number}")


if __name__ == "__main__":
    services = [
        {"service": "back_mobile", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "card_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "credentials_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "iabs_client_service", "con_type": "vpn", "team": "sme_credits", "env": "component"},
        {"service": "limit_module", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "onboarding_physical", "con_type": "vpn", "team": "sme_credits", "env": "component"},
        {"service": "reference_service", "con_type": "vpn", "team": "sme_credits", "env": "component"},
        {"service": "tariff_calculator", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "sme_credits", "con_type": "vpn", "team": "sme_credits", "env": "component"}
    ]

    process_jobs = []
    for num, item in enumerate(services):
        p = multiprocessing.Process(
            target=spawn_process,
            args=(num, item,)
        )
        process_jobs.append(p)
        p.start()

    for p in process_jobs:
        p.join()
