class IABSContext:
    iabs_client = None
    branches = None

    def __init__(self, iabs_id):
        self.iabs_id = iabs_id
