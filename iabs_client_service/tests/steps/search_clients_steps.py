import allure

from iabs_client_service.search_client.requests.search_client import IABSClientById
from utils.universal_steps.check_response import check_response_status, check_response_data_not_none
from unittest import TestCase as tc


@allure.step("Запрос на получения клиента IABS")
def step_iabs_client_by_id(client_uid):
    response = IABSClientById(client_uid).response()

    # Проверим в ответе запроса: status_code, наличие data
    check_response_status(response, expected_status="Success")
    check_response_data_not_none(response)

    data = response.data

    # Проверим на наличие всех атрибутов ответа на запрос
    check_client_uid(data)
    check_doc_type(data)
    check_doc_series(data)
    check_doc_number(data)
    check_doc_issued_at(data)
    check_doc_expires_at(data)
    check_doc_issued_by(data)
    check_pinfl(data)
    check_tin(data)
    check_last_name(data)
    check_first_name(data)
    check_middle_name(data)
    check_birth_date(data)
    check_birth_country_code(data)
    check_birth_place(data)
    check_gender(data)
    check_citizenship_country_code(data)
    check_branches(data)
    check_residence_country_code(data)
    check_residence_region_code(data)
    check_residence_district_code(data)
    check_residence_full_address(data)


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


@allure.step("doc_issued_by - не пустой")
def check_doc_issued_by(data):
    doc_issued_by = data["doc_issued_by"]
    tc().assertNotEqual(doc_issued_by, "", f"Поле ответа doc_issued_by ({doc_issued_by}) - пустой")


@allure.step("pinfl - не пустой")
def check_pinfl(data):
    pinfl = data["pinfl"]
    tc().assertNotEqual(pinfl, "", f"Поле ответа pinfl ({pinfl}) - пустой")


@allure.step("tin - не пустой")
def check_tin(data):
    tin = data["tin"]
    tc().assertNotEqual(tin, "", f"Поле ответа tin ({tin}) - пустой")


@allure.step("last_name - не пустой")
def check_last_name(data):
    last_name = data["last_name"]
    tc().assertNotEqual(last_name, "", f"Поле ответа last_name ({last_name}) - пустой")


@allure.step("first_name - не пустой")
def check_first_name(data):
    first_name = data["first_name"]
    tc().assertNotEqual(first_name, "", f"Поле ответа first_name ({first_name}) - пустой")


@allure.step("middle_name - не пустой")
def check_middle_name(data):
    middle_name = data["middle_name"]
    tc().assertNotEqual(middle_name, "", f"Поле ответа middle_name ({middle_name}) - пустой")


@allure.step("birth_date - не пустой")
def check_birth_date(data):
    birth_date = data["birth_date"]
    tc().assertNotEqual(birth_date, "", f"Поле ответа birth_date ({birth_date}) - пустой")


@allure.step("birth_country_code - не пустой")
def check_birth_country_code(data):
    birth_country_code = data["birth_country_code"]
    tc().assertNotEqual(birth_country_code, "",
                        f"Поле ответа birth_country_code ({birth_country_code}) - пустой")


@allure.step("birth_place - не пустой")
def check_birth_place(data):
    birth_place = data["birth_place"]
    tc().assertNotEqual(birth_place, "", f"Поле ответа birth_place ({birth_place}) - пустой")


@allure.step("gender - не пустой")
def check_gender(data):
    gender = data["gender"]
    tc().assertNotEqual(gender, "", f"Поле ответа gender ({gender}) - пустой")


@allure.step("citizenship_country_code - не пустой")
def check_citizenship_country_code(data):
    citizenship_country_code = data["citizenship_country_code"]
    tc().assertNotEqual(citizenship_country_code, "",
                        f"Поле ответа citizenship_country_code ({citizenship_country_code}) - пустой")


@allure.step("branches - не пустой")
def check_branches(data):
    branches = data["branches"]
    tc().assertNotEqual(branches, "", f"Поле ответа branches ({branches}) - пустой")


@allure.step("residence_country_code - не пустой")
def check_residence_country_code(data):
    residence_country_code = data["residence_country_code"]
    tc().assertNotEqual(residence_country_code, "",
                        f"Поле ответа residence_country_code ({residence_country_code}) - пустой")


@allure.step("residence_region_code - не пустой")
def check_residence_region_code(data):
    residence_region_code = data["residence_region_code"]
    tc().assertNotEqual(residence_region_code, "",
                        f"Поле ответа residence_region_code ({residence_region_code}) - пустой")


@allure.step("residence_district_code - не пустой")
def check_residence_district_code(data):
    residence_district_code = data["residence_district_code"]
    tc().assertNotEqual(residence_district_code, "",
                        f"Поле ответа residence_district_code ({residence_district_code}) - пустой")


@allure.step("residence_full_address - не пустой")
def check_residence_full_address(data):
    residence_full_address = data["residence_full_address"]
    tc().assertNotEqual(residence_full_address, "",
                        f"Поле ответа residence_full_address ({residence_full_address}) - пустой")
