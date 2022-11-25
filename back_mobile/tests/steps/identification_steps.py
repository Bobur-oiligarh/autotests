import allure

from back_mobile.test_data.db_models.dbo_signature import DBOSignature


@allure.step("Имитируем получение СМС кода (запрос в dbo_signature)")
def set_sms_code(context):
    context.code = DBOSignature().sms_key(context.sign_id)
