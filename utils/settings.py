from unittest import TestLoader, TestResult

from utils.patterns.singleton import Singleton
import multiprocessing


class SettingsBase:

    def __init__(self):
        self._ENV = None
        self._TEAM = None
        self._CON_TYPE = None
        self._SERVICE = None
        self._TESTS = None

    def set_data(self, data: dict):
        # print(f"set_data: {self.__dict__.values()}")
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


class Settings(SettingsBase, metaclass=Singleton):
    pass





