import allure

from back_mobile.requests.settings.put_change_language import PutChangeLanguage


@allure.step("сменить язык приложения change_language")
def step_change_language(context, lang_id: str = None):
    if lang_id:
        context.device.lang_id = lang_id
    response = PutChangeLanguage(context).response()
    response.check_success(context)
