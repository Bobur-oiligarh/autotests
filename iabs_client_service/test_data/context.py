
class IABSContext:

    iabs_client = None
    branches = None

    def __init__(self, iabs_id: str = None, data: dict = None):
        self.iabs_id = iabs_id
        self.data = data
