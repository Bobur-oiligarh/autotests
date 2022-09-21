import allure

from iabs_client_service.search_client.requests.search_client import IABSClientById
from utils.universal_steps.check_response import check_response
from unittest import  TestCase as tc

IABSClientID = "4959379"


@allure.step("Запрос на получения клиента IABS")
def iabs_client_by_id(client_id):
    response = IABSClientById(IABSClientID)
    check_response(response)    # Проверим в ответе запроса: status_code, наличие data
    data = response.data["data"]

    # Проверим на наличие всех атрибутов ответа на запрос
    check_client_uid()
    check_doc_type()
    check_doc_series()

@allure.step("client_uid - не пустой")
def check_client_uid(data):
    client_uid = data["client_uid"]
    tc().assertNotEqual(client_uid, "", f"Поле ответа client_uid ({client_uid}) - пустой")


@allure.step("doc_type - не пустой")
def check_doc_type(data):
    doc_type = data["doc_type"]
    tc().assertNotEqual(doc_type, "", f"Поле ответа doc_type ({doc_type}) - пустой")


@allure.step("doc_series - не пустой")
def check_doc_series(data):
    doc_series = data["doc_series"]
    tc().assertNotEqual(doc_series, "", f"Поле ответа doc_series ({doc_series}) - пустой")


@allure.step("doc_number - не пустой")
def check_doc_number(data):
    doc_number = data["doc_number"]
    tc().assertNotEqual(doc_number, "", f"Поле ответа doc_number ({doc_number}) - пустой")


@allure.step("doc_issued_at - не пустой")
def check_doc_issued_at(data):
    doc_issued_at = data["doc_issued_at"]
    tc().assertNotEqual(doc_issued_at, "", f"Поле ответа doc_issued_at ({doc_issued_at}) - пустой")


@allure.step("doc_expires_at - не пустой")
def check_doc_expires_at(data):
    doc_expires_at = data["doc_expires_at"]
    tc().assertNotEqual(doc_expires_at, "", f"Поле ответа doc_expires_at ({doc_expires_at}) - пустой")


"""
        "doc_number": "0356528",
        "doc_issued_at": "2021-05-04",
        "doc_expires_at": "2031-05-03",
        "doc_issued_by": "Qashqadaryo vil dexkonobod tumani IIB",
        "pinfl": "31209932580017",
        "tin": "530655303",
        "last_name": "KHUSANOV",
        "first_name": "MAKSADALI",
        "middle_name": "KHOLMAMATOVICH",
        "birth_date": "1993-09-12",
        "birth_country_code": "860",
        "birth_place": "Qashqadaryo vil dexkonobod tumani",
        "gender": "1",
        "citizenship_country_code": "860",
        "marital_status": "",
        "branches": [
            {
                "mfo": "01031",
                "client_code": "62229552"
            },
            {
                "mfo": "00083",
                "client_code": "62229552"
            },
            {
                "mfo": "01008",
                "client_code": "62229552"
            }
        ],
        "residence_country_code": "860",
        "residence_region_code": "10",
        "residence_district_code": "046",
        "residence_full_address": "Qashqadaryo vil dexkonobod tumani Boyqurgon",
        "residence_kadastr": ""
"""