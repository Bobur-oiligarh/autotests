from utils.api_utils.response_data_base import BaseTypeParent


class PutPrivateAddressToProspectDataType(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.address_id = data['id']

    def set_data_to(self, obj):
        pass

    def check(self, context, **kwargs):
        self.assert_not_empty_str('address_id')
