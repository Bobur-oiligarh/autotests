from utils.patterns.singleton import Singleton


class SettingsBase:

    def __init__(self):
        self._ENV = None
        self._TEAM = None
        self._CON_TYPE = None
        self._SERVICE = None
        self._TESTS = None
        self._PARAMS = None

    def set_data(self, data: dict):
        """
        data format: {
                "service" : "service_name",
                "env": "env_name",
                "team": "",
                "con_type": ""
            }
        """
        print(f"Settings.set_data, data = {data}")
        if None in self.__dict__.values():
            self._SERVICE = data.get("service")
            self._ENV = data.get("env")
            self._TEAM = data.get("team")
            self._CON_TYPE = data.get("con_type")
        return self

    def set_tests(self, data: dict):
        if not self._TESTS:
            self._TESTS = data.get("tests")
            self._PARAMS = data.get("params")

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
