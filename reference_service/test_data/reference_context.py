class ReferenceServiceContext:
    card_bins = None

    def __init__(self, card_number: str = None):
        self.card_number = card_number
