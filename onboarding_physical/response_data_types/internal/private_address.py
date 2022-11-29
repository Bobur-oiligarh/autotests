from utils.api_utils.response_data_base import BaseType
import allure


class PrivateAddress(BaseType):
    def __init__(self, data):
        super().__init__()
        self.address = data.get('address')
        self.block = data.get('block')
        self.country_code = data.get('country_code')
        self.created_at = data.get('created_at')
        self.district_code = data.get('district_code')
        self.flat = data.get('flat')
        self.house = data.get('house')
        self.id = data.get('id')
        self.kadastr = data.get('kadastr')
        self.place_desc = data.get('place_desc')
        self.profile_id = data.get('profile_id')
        self.region_code = data.get('region_code')
        self.registered_at = data.get('registered_at')
        self.street_desc = data.get('street_desc')
        self.type = data.get('type')

    def check(self, context, **kwargs):
        self.assert_not_empty_str('address')
        self.assert_no_strict_str('block')
        self.assert_no_strict_str('country_code')
        self.assert_no_strict_str('created_at')
        self.assert_no_strict_str('district_code')
        self.assert_no_strict_str('flat')
        self.assert_no_strict_str('house')
        self.assert_no_strict_str('id')
        self.assert_no_strict_str('kadastr')
        self.assert_no_strict_str('place_desc')
        self.assert_no_strict_str('profile_id')
        self.assert_no_strict_str('region_code')
        self.assert_no_strict_str('registered_at')
        self.assert_no_strict_str('street_desc')
        self.assert_no_strict_str('type')

    @allure.step('Установим данные адреса объекту')
    def set_data_to(self, obj):
        self._set_address_to(obj)

    def _set_address_to(self, obj):
        obj.private_address = self

    def get_data_to_put_request(self):
        data = dict()
        for item in ['id',
                     'profile_id',
                     'address',
                     'registered_at',
                     'country_code',
                     'region_code',
                     'district_code',
                     'kadastr',
                     'created_at']:
            data[item] = vars(self)[item]
        return data
