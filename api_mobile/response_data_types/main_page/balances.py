from api_mobile.response_data_types.response_data_base import BaseType


class Balances(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.balances: list
        self._set_balances(data)

    def _set_balances(self, data: dict):
        self.balances = []
        for balance in data:
            self.balances.append(balance)

    def check(self, client, **kwargs):
        pass


class Balance(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.balance = data["balance"]

    def check(self, client, **kwargs):
        pass
