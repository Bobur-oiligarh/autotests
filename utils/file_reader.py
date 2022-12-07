from utils.settings import Settings
from pathlib import Path


class FileReader:
    FILES = None
    ROOT_DIR = Path(__file__).parent.parent

    def get(self, file_name) -> list:
        file_path = self.ROOT_DIR.joinpath(f"{Settings().service()}/test_data/{file_name}")
        if ".csv" in file_name:
            return self._csv(file_path)

    @staticmethod
    def _csv(file_path):
        parameters = []
        with open(file_path, 'r') as file:
            for line in file:
                parameters.append(line.split(","))
        return parameters