"""Keeps IABSContext class."""


class IABSContext:
    """Class of IABS context type. """

    iabs_client = None
    branches = None

    def __init__(self, iabs_id):
        """Implements context by its id."""
        self.iabs_id = iabs_id
