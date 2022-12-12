from sme_make_decision_making.response_data_types.accounts import SMEAccounts, SMEAccount
from sme_make_decision_making.response_data_types.criterions import SMECriterions, SMECriterion
from sme_make_decision_making.response_data_types.strategies import SMEStrategy, SMEStrategies


class SMEContext:
    accounts: SMEAccounts = None
    account: SMEAccount = None

    criterions: SMECriterions = None
    criterion: SMECriterion = None

    strategy: SMEStrategy = None
    strategies: SMEStrategies = None
