class CredentialServiceContext:

    def __init__(self,
                 prospect_id: str = None,
                 device_id: str = None,
                 identity_sign: int = None,
                 language: str = None,
                 model: str = None,
                 phone: str = None):
        self.prospect_id = prospect_id
        self.device_id = device_id
        self.identity_sign = identity_sign
        self.language = language
        self.model = model
        self.phone = phone

        self.user_id: str = ""
        self.refresh_token: str = ""
        self.access_token: str = ""
