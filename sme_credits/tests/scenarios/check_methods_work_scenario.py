import allure

from sme_credits.tests.steps.account.delete_accounts_steps import step_delete_sme_accounts
from sme_credits.tests.steps.account.get_accounts_steps import step_get_sme_accounts
from sme_credits.tests.steps.account.patch_accounts_steps import step_patch_account
from sme_credits.tests.steps.account.post_accounts_steps import step_post_sme_accounts


def check_methods_work_scenario(context):
    # Достаём все SME аккаунты
    with allure.step(f"GET accounts"):
        pass
    step_get_sme_accounts(context)

    # Создаем новый аккаунт
    with allure.step(f"POST accounts/{context.id}"):
        pass
    created_account_id = step_post_sme_accounts(context)

    # Проверяем создался ли аккаунт
    with allure.step("Проверяем создался ли аккаунт"):
        pass
    step_get_sme_accounts(context)
    if context.accounts.is_account_exist(created_account_id):
        with allure.step(f"Аккаунт с id: {created_account_id} создался"):
            pass

    # Изменяем значение параметра аккаунта методом
    context.account.change_param(param_name="account_mask", param_value="11111")

    # Изменяем значение параметра аккаунта запросом PATCH
    with allure.step("Изменяем значение параметра аккаунта запросом PATCH"):
        pass
    step_patch_account(context)

    # Сопостовляем изменённый аккаунт
    step_get_sme_accounts(context)
    patched_account = context.accounts.get_account_by_param(param_name="id", param_value=context.account.id)
    if patched_account.equal(context.account):
        with allure.step(f"Аккаунты одинаковы. Значение параметра изменился успешно запросом PATCH"):
            pass

    # Удаляем аккаунт запросом DELETE
    step_delete_sme_accounts(context)

    # Проверяем удалился ли аккаунт успешно
    step_get_sme_accounts(context)
    if not context.accounts.is_account_exist(id=context.account.id):
        with allure.step(f"Аккаунт с id {context.account.id} удалился успешно"):
            pass
