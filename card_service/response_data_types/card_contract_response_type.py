from card_service.test_data.card_service_context import CardServiceContext
from utils.api_utils.response_data_base import BaseTypeParent
import allure


class CardContract(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.contract_id = data['contractId']
        self.client_uid = data['clientUid']
        self.client_id = data['clientId']
        self.embossed_name = data['embossedName']
        self.code_filial = data['codeFilial']
        self.account = data['account']
        self.contract_type = data['contractType']

    def check(self, context, **kwargs):
        self.assert_not_empty('contract_id')
        self.assert_not_empty('client_uid')
        self.assert_not_empty('client_id')
        self.assert_not_empty('embossed_name')
        self.assert_not_empty('account')
        self.assert_not_empty('contract_type')

    def set_data_to(self, obj: CardServiceContext):
        self._set_card_contract_to_obj(obj)

    @allure.step('Установим контракт карты объекту')
    def _set_card_contract_to_obj(self, obj):
        obj.card_contract = self
