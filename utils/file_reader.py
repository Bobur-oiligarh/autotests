from utils.settings import Settings
from pathlib import Path


class FileReader:
    FILES = None
    ROOT_DIR = Path(__file__).parent.parent

    def get(self, file_name) -> list[dict]:
        file_path = self.ROOT_DIR.joinpath(f"{Settings().service()}/test_data/{file_name}")
        if ".csv" in file_name:
            return self._csv(file_path)

    def _csv(self, file_path) -> list[dict]:
        table = []
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                table.append(line.split(","))
            return self._table_to_dict_list(table)

    def _table_to_dict_list(self, table: list) -> list[dict]:
        parameters = []
        coll_names = table[0]
        for num, line in enumerate(table):
            if num == 0:
                continue
            line_dict = {}
            for index, coll in enumerate(line):
                line_dict[coll_names[index]] = self._convert_type(coll)
            parameters.append(line_dict)
        return parameters

    @staticmethod
    def _convert_type(value: str) -> str | int | float | bool | None:

        if re.fullmatch(r"^\d+\.\d+$", value):
            return float(value)

        if re.fullmatch(r"^\d+$", value):
            return int(value)

        if re.fullmatch(r"([A-Za-zА-Яа-я]\s*.*)+", value):

            if re.fullmatch(r"^True|False$", value):
                return bool(value)

            return str(value)
        return None


if __name__ == '__main__':
    f = FileReader().get("vbnv_118.csv")
    print(f)
