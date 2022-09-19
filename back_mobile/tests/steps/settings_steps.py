import allure

from back_mobile.requests.settings.change_language import ChangeLanguage
from utils.universal_steps.check_response import check_response


@allure.step("сменить язык приложения change_language")
def step_change_language(client, lang_id: str = None):
    if lang_id:
        client.device.lang_id = lang_id
    response = ChangeLanguage(client).response()
    check_response(response, client)
