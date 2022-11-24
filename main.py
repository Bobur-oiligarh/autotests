import multiprocessing

from utils.settings import Settings
from _pytest.config import main as pt_main


def set_tests_from_params(command: list, service_name, tests: list):
    for item in tests:
        command.append(f"./{service_name}/tests/test_cases/{item}_test.py")


def set_tests(command: list, params: dict):
    if params.get("tests"):
        set_tests_from_params(command, params["service"], params["tests"])
        return
    command.append(f"./{params['service']}/tests/test_cases/demo_test.py")


def spawn_process(number, params: dict):
    print(f"Process number - {number}")
    Settings().set_data(params)
    command = []
    set_tests(command, params)
    command.append("--alluredir")
    command.append("./results")
    command.append("-v")
    print(f"Testing of service {params['service']} is started")
    pt_main(command)


def create_test_process(number, params):
    process = multiprocessing.Process(
        target=spawn_process,
        args=(number, params,)
    )
    process.start()
    return process


if __name__ == "__main__":
    services = [
        # {"service": "back_mobile", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "card_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        {"service": "credentials_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "iabs_client_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "limit_module", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "onboarding_physical", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "reference_service", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "tariff_calculator", "con_type": "vpn", "team": "hamkor_mobile", "env": "component"},
        # {"service": "sme_credits", "con_type": "vpn", "team": "sme_credits", "env": "component", "tests": ["vbnv_100"]}
    ]
    process_jobs = []
    for num, item in enumerate(services):
        process_jobs.append(create_test_process(num, item))

    for p in process_jobs:
        p.join()
