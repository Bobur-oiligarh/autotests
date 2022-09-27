class CardServiceContext:
    cards = None

    def __init__(self, phone_number: str = None):
        self.phone_number = phone_number
