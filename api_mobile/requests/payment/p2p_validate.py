from api_mobile.response_data_types.payment.p2p_validate_result import P2PValidateResult
from api_mobile.response_data_types.payment.templates import TransactionParticipant, Template
from api_mobile.test_data.client import Client
from utils.api_utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PValidate(TestRequest):

    def __init__(
            self,
            client: Client,
            summ: float,
            template: Template = None,
            receiver: TransactionParticipant = None
    ):

        super().__init__(
            URLProvider().url("back_mobile", "payment", "p2p_validate"),
            data_type=P2PValidateResult,
            headers=client.auth_token()
        )

        self.sender: TransactionParticipant = self._set_sender(client, template)
        self.receiver: TransactionParticipant = receiver if receiver else template.receiver
        self.sum: float = summ
        self.template_id = template.template_id if template else ""

    @staticmethod
    def _set_sender(client: Client, template: Template = None) -> TransactionParticipant:
        if not template:
            return TransactionParticipant({
                "id": client.main_card.card_id,
                "pan": client.main_card.mask_num,
                "expire": client.main_card.expire,
                "ps_code": client.main_card.ps_code,
                "bank_code": client.main_card.mfo,
                "owner": client.main_card.owner
            })
        else:
            return template.sender
