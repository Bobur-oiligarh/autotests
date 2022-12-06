from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class DeleteCriterion(TestRequest):
    def __init__(self, context):
        super().__init__(
            url=URLProvider().url(
                service_name="sme_make_decision_making",
                end_point=f"criterions/{context.criterion.id}"
            ),
            method="delete",
            data_type=None,
            require_err_note=False
        )