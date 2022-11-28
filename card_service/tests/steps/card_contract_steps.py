import allure

from card_service.requests.post_card_contract import PostCardContract


@allure.step('Запрос контракта для карта по его номеру')
def step_get_and_check_card_contract(context):
    response = PostCardContract(context).response()
    response.check_success(context).data.set_data_to(context)
