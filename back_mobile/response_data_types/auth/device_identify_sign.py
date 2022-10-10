from back_mobile.response_data_types.registration import AccRefTokens

__all__ = [
    "DeviceIdentifySign"
]


class DeviceIdentifySign(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.device_identify_sign = data["device_identify_sign"]

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        self.assert_not_empty_int("device_identify_sign")
