class CardServiceContext:
    cards = None
    card_contract = None

    def __init__(self, phone: str = None, card_number: str = None, bins: list = None,
                 iabs_client_id: str = None, prospect_id: str = None):
        self.phone = phone
        self.card_number = card_number
        self.bins = bins
        self.iabs_client_id = iabs_client_id
        self.prospect_id = prospect_id
