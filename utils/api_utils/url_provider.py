from back_mobile.test_data.back_mobile_urls import back_mobile_urls
from card_service.test_data.card_service_urls import card_service_urls
from credentials_service.test_data.credential_service_urls import credentials_service
from iabs_client_service.test_data.iabs_clients_service_urls import iabs_clients_service
import os

from limit_module.test_data.limit_module_urls import limit_module_urls
from onboarding_physical.test_data.onboarding_physical_urls import onboarding_physical_urls
from limit_module.test_data.limit_module_urls import limit_module_urls
from reference_service.test_data.reference_service_urls import reference_service_urls
from tariff_calculator.test_data.tariff_calculator_urls import tariff_calculator_urls
from utils.patterns.singleton import Singleton

all_services_urls = {
    "back_mobile": back_mobile_urls,
    "card_service": card_service_urls,
    "tariff_calculator": tariff_calculator_urls,
    "iabs_clients_service": iabs_clients_service,
    "reference_service": reference_service_urls,
    "credentials_service": credentials_service,
    "limit_module": limit_module_urls,
    "onboarding_physical": onboarding_physical_urls
    "reference_service": reference_service_urls,
    "credentials_service": credentials_service,
    "limit_module": limit_module_urls
}


class URLProviderBase:

    def url(self, service_name, function_name, end_point, end_of_path: str = "") -> dict:
        urls = all_services_urls[service_name]
        url = {
            "url": self._environment(urls) + urls[function_name][end_point]["path"] + end_of_path,
            "method": urls[function_name][end_point]["method"]
        }
        return url

    @staticmethod
    def _environment(urls) -> str:
        if len(urls["environment"]["all"]) > 0:
            return urls["environment"]["all"]
        return urls["environments"][os.environ["ENVIRONMENT"]]


class URLProvider(URLProviderBase, metaclass=Singleton):
    pass
