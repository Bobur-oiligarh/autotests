import allure

from back_mobile.requests.payment.post_p2p_confirm import PostP2PConfirm
from back_mobile.requests.payment.get_p2p_info import GetP2PInfo
from back_mobile.requests.payment.post_p2p_init import PostP2PInit
from back_mobile.requests.payment.get_p2p_templates import GetP2PTemplates
from back_mobile.requests.payment.post_p2p_validate import PostP2PValidate


@allure.step("Запрос шаблонов переводов templates")
def step_p2p_templates(context):
    response = GetP2PTemplates(context).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Запрос информации по карте получателя p2p_info")
def step_p2p_info(context, card_number: str):
    response = GetP2PInfo(context, card_number).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Валидация перевода по карте пользователя p2p_validate")
def step_card_p2p_validate(context):
    response = PostP2PValidate(context, summ=1000, receiver=context.receiver).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Валидация перевода по шаблону p2p_validate")
def step_template_p2p_validate(context):
    response = PostP2PValidate(context, summ=1000, template=context.templates.templates[0]).response()
    response.check_success(context).data.set_data_to(context)


@allure.step("Инициализация перевода p2p_init")
def step_p2p_init(client):
    response = PostP2PInit(client).response()
    response.check_success(client).data.set_data_to(client)


@allure.step("Подтверждение перевода p2p_confirm")
def step_p2p_confirm(client, confirm_code=""):
    response = PostP2PConfirm(client, confirm_code).response()
    response.check_success(client).data.set_data_to(client)
