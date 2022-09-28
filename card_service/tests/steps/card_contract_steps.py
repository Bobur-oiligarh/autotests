import allure

from card_service.requests.card_contract_requests import CardContractRequest


@allure.step('Запрос контракта для карта по его номеру')
def step_get_and_check_card_contract(context):
    response = CardContractRequest(context).response()
    response.check_success(context).data.set_data_to(context)
