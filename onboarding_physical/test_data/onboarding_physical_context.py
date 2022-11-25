class OnboardingPhysicalContext:

    prospect_profile = None
    prospect = None
    prospect_by_phone_iabs = None
    private_contact = None
    private_prospect = None
    private_address = None

    def __init__(self,
                 prospect_id: str = None,
                 iabs_id: str = None,
                 phone: str = None,
                 contact_type: str = None,
                 contact_id: str = None,
                 address_id: str = None):
        self.prospect_id = prospect_id
        self.iabs_id = iabs_id
        self.phone = phone
        self.contact_type = contact_type
        self.contact_id = contact_id
        self.address_id = address_id
