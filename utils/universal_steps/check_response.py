import allure

from api_mobile.test_data.client import Client
from utils.api_utils.test_response import TestResponse
from unittest import TestCase


@allure.step("Проверка ответа")
def check_response(response: TestResponse, client: Client, expired_status: str = "Success", **kwargs):
    check_response_status(response, expired_status)
    check_response_data_not_none(response)
    check_response_data(response, client, **kwargs)


@allure.step("Проверка статуса ответа")
def check_response_status(response: TestResponse, expired_status: str = "Success"):
    tc = TestCase()
    tc.assertEqual(response.status, expired_status,
                   f"Статус ответа ({response.status}) не соответствует "
                   f"ожидаемому ({expired_status})" + response.__str__())


@allure.step("Проверка data ответа")
def check_response_data_not_none(response: TestResponse):
    tc = TestCase()
    tc.assertIsNotNone(response.data, f"Параметр data ответа является None" + response.__str__())


@allure.step("Проверка параметров данных ответа")
def check_response_data(response: TestResponse, client: Client, **kwargs):
    response.data.check(client, **kwargs)
