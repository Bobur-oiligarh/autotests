
class IABSClient:
    """Creates IABS client class."""

    doc_type = None
    doc_series = None
    doc_number = None
    doc_issued_at = None
    doc_expires_at = None
    doc_issued_by = None
    pinfl = None
    tin = None
    last_name = None
    first_name = None
    middle_name = None
    birth_date = None
    birth_country_code = None
    birth_place = None
    gender = None
    citizenship_country_code = None
    marital_status = None
    branches = None
    residence_country_code = None
    residence_region_code = None
    residence_district_code = None
    residence_full_address = None
    residence_kadastr = None

    def __init__(self, client_id):
        """Initializes an iabs client object. """
        self.client_uid = client_id
