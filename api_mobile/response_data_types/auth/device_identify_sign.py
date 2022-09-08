import allure

from api_mobile.response_data_types.registration import AccRefTokens


class DeviceIdentifySign(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.device_identify_sign = data["device_identify_sign"]

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        self.device_identify_sign_not_null()

    @allure.step("device_identify_sign не null")
    def device_identify_sign_not_null(self):
        self._tc.assertIsNotNone(self.device_identify_sign,
                                 f"device_identify_sign является null" + self.__str__())
