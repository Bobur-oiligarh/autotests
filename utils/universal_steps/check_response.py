import allure

from utils.api_utils.test_response import TestResponse
from unittest import TestCase


@allure.step("Проверка статуса ответа")
def check_response_status(response: TestResponse = None, status: str = "Success"):
    tc = TestCase()
    tc.assertEqual(response.status, status, response)
