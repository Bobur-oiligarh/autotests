from unittest import TestCase

from tariff_calculator.test_data.tariff_calculator_context import TariffCalcContext, P2PParticipant
from tariff_calculator.tests.steps.calc_p2p_comm_steps import calculate_p2p_commission


class TariffCalcDemo(TestCase):

    def setUp(self) -> None:
        self.context = TariffCalcContext(
            channel_id="mobilebank",
            iabs_id="test",
            product_id="p2p",
            sum=500000000,
            sender=P2PParticipant(
                id="9074192C56C900EAE053C0A865A6A81A",
                number="860012",
                bank_code="09012",
                ps_code="UZCARD"
            ),
            receiver=P2PParticipant(
                id="9074192C56C900EAE053C0A865A6A81A",
                number="860012",
                bank_code="09012",
                ps_code="UZCARD"
            )
        )

    def test_p2p_commission(self):
        calculate_p2p_commission(self.context)

