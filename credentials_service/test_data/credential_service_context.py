class CredentialServiceContext:

    device_info = None

    def __init__(self,
                 prospect_id: str = None,
                 device_id: str = None,
                 identity_sign: int = None,
                 language: str = None,
                 model: str = None,
                 phone: str = None,
                 i_abs_code: str = None,
                 i_abs_id: str = None,
                 user_id: str = None):
        self.prospect_id = prospect_id
        self.device_id = device_id
        self.identity_sign = identity_sign
        self.language = language
        self.model = model
        self.phone = phone
        self.i_abs_code = i_abs_code
        self.i_abs_id = i_abs_id

        self.user_id: str = user_id
        self.refresh_token: str = ""
        self.access_token: str = ""
