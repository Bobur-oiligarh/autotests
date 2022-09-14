from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class Cards(BaseTypeParent):
    """
    {
            "card_id": "9074192C56C900EAE053C0A865A6A81A",
            "card_type": "private",
            "mfo": "09012",
            "mask_num": "860012******0615",
            "state": "active",
            "balance": 1084526.91,
            "ps_code": "UZCARD",
            "expire": "1249",
            "owner": "MAQSADALI H."
    }
    """

    def __init__(self, data: list):
        super().__init__()
        self.cards_list = self.deserialize_to_list_of(Card, data)

    def set_data_to(self, obj):
        pass

    def check(self, client, **kwargs):
        pass


class Card(BaseType):
    """
    {
        "card_id": "9074192C56C900EAE053C0A865A6A81A",
        "card_number": "860012******0615",
        "owner": "MAQSADALI HUSANOV",
        "balance": 108452691,
        "hold_amount": 0,
        "state": "active",
        "card_type": "private",
        "processing": "UZCARD",
        "account": "0101322618000399046188001",
        "expire": "1249",
        "bank_code": ""
    }
    """

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.card_number = data["card_number"]

    def check(self, client, **kwargs):
        pass
