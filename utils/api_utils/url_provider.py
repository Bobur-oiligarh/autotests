import os

from utils.patterns.singleton import Singleton
from utils.yaml_reader import YAMLReader


class URLProviderBase:

    def __init__(self):
        self.paths = YAMLReader().paths
        self.hosts = {
            "component": self._component_env(),
            "integration": self._integration_env()
        }

    def url(self, service_name, end_point) -> str:
        return f"http://{self._path(service_name)}/{end_point}"

    def db_url(self):
        return f"{self._path('postgres')}"

    def _path(self, service_name):
        return f"{self.hosts[os.environ['ENV']]}:{self._port(service_name)}"

    def _port(self, service_name) -> str:
        return self.paths["ports"][service_name]

    def _integration_env(self) -> str:
        return f"{self.paths['hosts']['integration'][os.environ['CONNECTION']]}:"

    def _component_env(self) -> str:
        return f"{self.paths['hosts']['component']['prefix'][os.environ['CONNECTION']]}" \
               f"{self.paths['hosts']['component']['suffix'][os.environ['TEAM']]}"


class URLProvider(URLProviderBase, metaclass=Singleton):
    pass
