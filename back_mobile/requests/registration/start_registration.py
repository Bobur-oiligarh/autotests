from back_mobile.response_data_types.registration.sign_id import SignId
from utils.api_utils.test_request import TestRequest
from back_mobile.test_data.client import Client, User, Device
from utils.api_utils.url_provider import URLProvider


class StartRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("back_mobile", "api/v1/mobile/start-registration"),
            "post",
            data_type=SignId
        )

        self.phone = client.user.phone_number
        self.phone_type = client.device.phone_type
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.lang_id = client.device.lang_id
        self.app_version = client.app_version


if __name__ == "__main__":
    print(StartRegistration(Client(
        User(
            "998941775859",
            "8600120480409831",
            "0923",
            residence_of_uz=False
        ),
        Device(
            phone_type="1",
            device_id="string7",
            device_info="string7",
            device_os="Android",
            lang_id="ru"
        )
    )).response())
