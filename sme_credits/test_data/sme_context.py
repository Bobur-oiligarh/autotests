class SMEContext:
    accounts = None

    def __init__(self, account_mask: str = None, active: bool = True, list_id: str = None, user_employee: str = None):
        self.account_mask = account_mask
        self.active = active
        self.list_id = list_id
        self.user_employee = user_employee
