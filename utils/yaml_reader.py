import yaml
from pathlib import Path

from utils.patterns.singleton import Singleton


class YAMLReader(metaclass=Singleton):
    CRED_PATH = Path(__file__).parent.parent.joinpath("credentials.yaml")

    def __init__(self):
        self.paths: dict = self.read()["paths"]
        self.minio: dict = self.read()["minio"]
        self.rabbit: dict = self.read()["rabbit"]

    def read(self):
        with open(self.CRED_PATH, "r") as f:
            read_data = yaml.load(f, Loader=yaml.FullLoader)
        return read_data
