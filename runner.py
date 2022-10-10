import os

from dotenv import load_dotenv


def run(test_dir):
    os.system(f"python -m pytest ./{test_dir}/tests/test_cases/ --alluredir ./results -v")


if __name__ == "__main__":
    load_dotenv()
    for key in os.environ.keys():
        if key.startswith("TEST_DIR"):
            run(os.environ.get(key))
