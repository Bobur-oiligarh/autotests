from utils.patterns.singleton import Singleton
from utils.settings import Settings
from utils.yaml_reader import YAMLReader


class URLProviderBase:

    def __init__(self):
        self._s = Settings()
        self.paths = YAMLReader().paths
        self.hosts = {
            "component": self._component_env(),
            "integration": self._integration_env()
        }

    def url(self, service_name, end_point) -> str:
        return f"http://{self._path(service_name)}/{end_point}"

    def db_url(self):
        return f"{self._path('postgres')}"

    def rabbit_url(self):
        pass

    def _path(self, service_name):
        return f"{self.hosts[self._s.env()]}:{self._port(service_name)}"

    def _port(self, service_name) -> str:
        return self.paths["ports"][service_name]

    def _integration_env(self) -> str:
        return f"{self.paths['hosts']['integration'][self._s.con_type()]}:"

    def _component_env(self) -> str:
        return f"{self.paths['hosts']['component']['prefix'][self._s.con_type()]}" \
               f"{self.paths['hosts']['component']['suffix'][self._s.team()]}"


class URLProvider(URLProviderBase, metaclass=Singleton):
    pass
