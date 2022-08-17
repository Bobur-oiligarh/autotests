import base64

from api_mobile.response_data_types.registration_data_types import SignId, AccRefTokens, Offer, AgreeOfferResult, \
    ConfirmMethod, StoreAccRefTokens
from utils.db.models.dbo_signature import DBOSignature
from utils.test_data.providers import URLProvider
from utils.test_data.client import Client, User, Device
from utils.api_utils.test_request import TestRequest


class StartRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "start_reg"),
            data_type=SignId
        )

        self.phone = client.user.phone_number
        self.phone_type = client.device.phone_type
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.lang_id = client.device.lang_id
        self.app_version = client.app_version


class FinishRegistration(TestRequest):

    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "finish_reg"),
            data_type=AccRefTokens
        )
        self.code = client.code
        self.device_id = client.device.device_id
        self.device_info = client.device.device_info
        self.lang_id = client.device.lang_id
        self.sign_id = client.sign_id


class GetOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "get_offer"),
            data_type=Offer,
            headers=client.auth_token()
        )


class AgreeOffer(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "agree_offer"),
            data_type=AgreeOfferResult,
            headers=client.auth_token()
        )
        self.action = client.action


class CheckClientReg(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider().url("registration", "check_client_reg"),
            data_type=ConfirmMethod,
            headers=client.auth_token()
        )
        self.card_number = client.user.card_number
        self.date_expire = client.user.date_expire
        self.device_info = client.device.device_info
        self.device_os = client.device.device_os
        self.app_version = client.app_version


class BioIdentification(TestRequest):
    def __init__(self, client: Client):
        super().__init__(
            URLProvider.url(),
            data_type=StoreAccRefTokens
        )
        self.birth_date = client.user.birth_date
        self.doc_number = client.user.doc_number
        self.doc_series = client.user.doc_series
        self.doc_type = client.user.doc_type
        self.photo = {"front": "" + base64.b64encode(client.photo)}


if __name__ == "__main__":
    client = Client(
        User(
            "998935087121",
            "8600120436901998",
            "1023"
        ),
        Device(
            phone_type="1",
            device_id="string7",
            device_info="string7",
            device_os="Android",
            lang_id="ru"
        )
    )

    print()
    print("StartRegistration")
    sr = StartRegistration(client=client)
    print(sr.get_response())
    client.sign_id = sr.get_response().data.sign_id
    client.code = DBOSignature().sms_key(client.sign_id)

    print()
    print("FinishRegistration")
    fr = FinishRegistration(client=client)
    print(fr.get_response())
    client.refresh_token = fr.get_response().data.refresh_token
    client.access_token = fr.get_response().data.access_token
    print(client)

    # time.sleep(3)
    print()
    print("GetOffer")
    go = GetOffer(client=client)
    print(go.get_response())

    print()
    print("AgreeOffer")
    ao = AgreeOffer(client)
    print(ao.get_response())

    print()
    print("CheckClientReg")
    ccr = CheckClientReg(client=client)
    print(ccr.get_response())

    # print(pp())

    # print(client)
