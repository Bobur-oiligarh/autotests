from sme_make_decision_making.response_data_types.criterions import SMECriterion, SMECriterions
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class GetCriterions(TestRequest):
    def __init__(self):
        super().__init__(
            url=URLProvider().url(service_name="sme_make_decision_making", end_point="criterions"),
            method="get",
            data_type=SMECriterions,
            require_err_note=False
        )

class GetCriterion(TestRequest):

    def __init__(self, criterion_id):
        super().__init__(
            url=URLProvider().url(service_name="sme_make_decision_making", end_point=f"criterions/{criterion_id}"),
            method="get",
            data_type=SMECriterion,
            require_err_note=False
        )
