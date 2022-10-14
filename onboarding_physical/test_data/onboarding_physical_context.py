
class OnboardingPhysicalContext:
    prospect_profile = None
    prospect = None

    def __init__(self, prospect_id: str, iabs_id: str):
        self.prospect_id = prospect_id
        self.iabs_id = iabs_id
