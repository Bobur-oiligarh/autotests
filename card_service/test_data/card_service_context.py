class CardServiceContext:
    cards = None
    card_contract = None

    def __init__(self, phone_number: str = None, card_number: str = None):
        self.phone_number = phone_number
        self.card_number = card_number
