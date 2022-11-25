from back_mobile.response_data_types.payment.p2p_validate import P2PValidate
from back_mobile.response_data_types.payment.templates import TransactionParticipant, Template
from utils.url_provider import URLProvider
from utils.api_utils.test_request import TestRequest


class PostP2PValidate(TestRequest):

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
            data_type=P2PValidate,
            headers=context.auth_token()
        )

        self.sender: TransactionParticipant = self._set_sender(context, template)
        self.receiver: TransactionParticipant = receiver if receiver else template.receiver
        self.sum: float = summ
        self.template_id = template.template_id if template else ""

    @staticmethod
    def _set_sender(context, template: Template = None) -> TransactionParticipant:
        if not template:
            return TransactionParticipant({
                "id": context.main_card.card_id,
                "pan": context.main_card.mask_num,
                "expire": context.main_card.expire,
                "ps_code": context.main_card.ps_code,
                "bank_code": context.main_card.mfo,
                "owner": context.main_card.owner
            })
        else:
            return template.sender
