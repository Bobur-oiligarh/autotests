from back_mobile.response_data_types.payment.p2p_validate_result import P2PValidateResult
from back_mobile.response_data_types.payment.templates import TransactionParticipant, Template
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class P2PValidate(TestRequest):

    def __init__(
            self,
            context,
            summ: float,
            template: Template = None,
            receiver: TransactionParticipant = None
    ):

        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/payment/p2p-validate"),
            "post",
            data_type=P2PValidateResult,
            headers=context.auth_token()
        )

        self.sender: TransactionParticipant = self._set_sender(context, template)
        self.receiver: TransactionParticipant = receiver if receiver else template.receiver
        self.sum: float = summ
        self.template_id = template.template_id if template else ""

    @staticmethod
    def _set_sender(client, template: Template = None) -> TransactionParticipant:
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
