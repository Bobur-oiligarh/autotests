class P2PParticipant:

    def __init__(self, id: str, number: str, bank_code: str, ps_code: str):
        self.id = id
        self.number = number
        self.bank_code = bank_code
        self.ps_code = ps_code


class TariffCalcContext:
    p2p_commission = None

    def __init__(self, channel_id: str, iabs_id: str, product_id: str, sum: int, sender: P2PParticipant, receiver):
        self.channel_id = channel_id
        self.iabs_id = iabs_id
        self.product_id = product_id
        self.sum = sum
        self.sender = sender.__dict__
        self.receiver = receiver.__dict__
