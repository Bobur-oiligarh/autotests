from back_mobile.response_data_types.registration.access_refresh_tokens import AccRefTokens

__all__ = [
    "DeviceIdentifySign"
]


class DeviceIdentifySign(AccRefTokens):
    def __init__(self, data: dict):
        super().__init__(data)
        self.device_identify_sign = data["device_identify_sign"]

    def check(self, context, **kwargs):
        super().check(context, **kwargs)
        self.assert_not_empty_int("device_identify_sign")
