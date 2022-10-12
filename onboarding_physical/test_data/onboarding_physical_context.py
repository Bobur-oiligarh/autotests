
class OnboardingPhysicalContext:
    prospect_profile = None
    prospect = None

    def __init__(self, prospectID: str, iabs_id: str):
        self.prospectID = prospectID
        self.iabs_id = iabs_id
