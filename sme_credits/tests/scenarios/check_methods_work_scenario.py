import allure

from sme_credits.tests.steps.account.delete_accounts_steps import step_delete_sme_accounts
from sme_credits.tests.steps.account.get_accounts_steps import step_get_sme_accounts
from sme_credits.tests.steps.account.patch_accounts_steps import step_patch_account
from sme_credits.tests.steps.account.post_accounts_steps import step_post_sme_accounts


@allure.step("Проверка работы конечных точек SME accounts")
def check_methods_work_scenario(context):
    step_get_sme_accounts(context)
    step_post_sme_accounts(context)
    step_get_sme_accounts(context)
    context.accounts.account_exist(context.account.id)
    context.account.change_param(param_name="account_mask", param_value="11111")
    step_patch_account(context)
    step_get_sme_accounts(context)
    context.account.assert_equal(
        context.accounts.get_account_by_param(param_name="id", param_value=context.account.id)
    )
    step_delete_sme_accounts(context)
    step_get_sme_accounts(context)
    context.accounts.account_not_exist(context.account.id)
