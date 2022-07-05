from utils.methods import obj_to_string


class User:

    def __init__(self, phone_number: str,
                 card_number: str,
                 date_expire: str,
                 birth_date: str = None,
                 doc_number: str = None,
                 doc_series: str = None,
                 doc_type: str = None,
                 photo: dict = None):
        self.phone_number = phone_number
        self.card_number = card_number
        self.date_expire = date_expire
        self.birth_date = birth_date
        self.doc_number = doc_number
        self.doc_series = doc_series
        self.doc_type = doc_type
        self.photo = photo

    def __str__(self):
        return obj_to_string(self)


class Device:

    def __init__(self, phone_type: str, device_id: str, device_info: str, device_os: str, lang_id: str):
        self.phone_type = phone_type
        self.device_id = device_id
        self.device_info = device_info
        self.device_os = device_os
        self.lang_id = lang_id

    def __str__(self):
        return obj_to_string(self)


class Client:
    first_name: str
    last_name: str
    middle_name: str

    user: User
    device: Device

    sign_id: str
    code: str

    access_token: str
    refresh_token: str
    confirm_method: str

    app_version: str

    def __init__(self, user: User, device: Device, app_version: str = "1.0.1", action: str = "accept"):
        self.user = user
        self.device = device
        self.app_version = app_version
        self.action = action

    def auth_token(self) -> dict:
        return {"Authorization": "Bearer " + self.access_token}

    def __str__(self):
        return "\nClient\n" + obj_to_string(self) + "\n"