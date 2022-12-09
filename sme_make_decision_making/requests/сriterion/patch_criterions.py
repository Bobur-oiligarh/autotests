from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PatchCriterion(TestRequest):
    def __init__(self, context):
        super().__init__(
            url=URLProvider().url(
                service_name="sme_make_decision_making",
                end_point=f"criterions/{context.criterion.id}"
            ),
            data_type=None,
            method="patch",
            require_err_note=False
        )
        self.active = context.criterion.active
        self.amount_check = context.criterion.amount_check
        self.count_check = context.criterion.count_check
        self.date_action = context.criterion.date_action
        self.date_check = context.criterion.date_check
        self.list_id = context.criterion.list_id
        self.name = context.criterion.name
        self.points = context.criterion.points
        self.step_id = context.criterion.step_id
