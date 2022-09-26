from utils.methods import obj_to_string


class User:

    def __init__(self, phone_number: str,
                 card_number: str,
                 date_expire: str,
                 birth_date: str = None,
                 doc_number: str = None,
                 doc_series: str = None,
                 doc_type: str = None,
                 photo: dict = None,
                 residence_of_uz: bool = True):
        self.phone_number = phone_number
        self.card_number = card_number
        self.date_expire = date_expire
        self.birth_date = birth_date
        self.doc_number = doc_number
        self.doc_series = doc_series
        self.doc_type = doc_type
        self.photo = photo
        self.residence_of_uz = residence_of_uz

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
    first_name: str = None

    last_name: str = None
    middle_name: str = None

    user: User = None
    device: Device = None

    cards = None
    main_card = None
    operations = None

    templates = None
    receiver = None
    p2p_validate_result = None
    operation_check = None

    atm_list = None
    branches = None
    lang_list = None
    operators = None
    exchange_rates = None

    loans = None
    accounts = None
    deposits = None
    webview_link = None

    sign_id: str = None
    code: str = None

    access_token: str = None
    refresh_token: str = None
    confirm_method: str = None

    app_version: str = None

    def __init__(self, user: User, device: Device, app_version: str = "1.0.1", offer_sign_action: str = "accept",
                 p2p_init_action: str = "accept", region_code: str = "10"):
        self.user = user
        self.device = device
        self.app_version = app_version
        self.offer_sign_action = offer_sign_action
        self.p2p_init_action = p2p_init_action
        self.expected_confirm_method = "BIO" if user.residence_of_uz else "SMS"
        self.region_code = region_code

    def get_by_name(self, name: str):
        result = getattr(self, name, None)
        if result is None:
            result = getattr(self.device, name, None)
        if result is None:
            result = getattr(self.user, name, None)
        return result

    def auth_token(self) -> dict:
        return {"Authorization": "Bearer " + self.access_token}

    def __str__(self):
        return "\nClient" + obj_to_string(self) + "\n"
