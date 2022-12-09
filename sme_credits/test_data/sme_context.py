from sme_credits.response_data_types.account.accounts import SMEAccounts, SMEAccount
from sme_credits.response_data_types.list.lists import SMEList, SMELists
from sme_credits.response_data_types.strategy.strategies import SMEStrategy, SMEStrategies


class SMEContext:
    accounts: SMEAccounts = None
    account: SMEAccount = None

    strategy: SMEStrategy = None
    strategies: SMEStrategies = None

    list: SMEList = None
    lists: SMELists = None
    list_accounts: SMEAccounts = None
