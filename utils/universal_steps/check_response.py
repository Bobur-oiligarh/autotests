import allure

from api_mobile.test_data.client import Client
from utils.api_utils.test_response import TestResponse
from unittest import TestCase as tc


@allure.step("Проверка ответа")
def check_response(response: TestResponse, client: Client, expected_status: str = "Success", **kwargs):
    check_response_status(response, expected_status)
    check_response_data_not_none(response)
    check_response_data(response, client, **kwargs)


@allure.step("Проверка статуса ответа")
def check_response_status(response: TestResponse, expected_status: str = "Success"):
    tc.assertEqual(response.status, expected_status,
                   f"Статус ответа ({response.status}) не соответствует "
                   f"ожидаемому ({expected_status})" + response.__str__())


@allure.step("Проверка data ответа")
def check_response_data_not_none(response: TestResponse):
    tc.assertIsNotNone(response.data, f"Параметр data ответа является None" + response.__str__())


@allure.step("Проверка параметров данных ответа")
def check_response_data(response: TestResponse, client: Client, **kwargs):
    response.data.check(client, **kwargs)
