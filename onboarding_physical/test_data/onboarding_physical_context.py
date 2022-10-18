class OnboardingPhysicalContext:

    prospect_profile = None
    prospect = None
    prospect_by_phone_iabs = None
    private_contact = None

    def __init__(self, prospect_id: str = None, iabs_id: str = None, phone: str = None, contact_type: str = None):
        self.prospect_id = prospect_id
        self.iabs_id = iabs_id
        self.phone = phone
        self.contact_type = contact_type
