from utils.api_utils.response_data_base import BaseTypeParent


class SMECriterions(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.criterions: list[SMECriterion] = self.deserialize_to_list_of(SMECriterion, data)

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    def set_data_to_context(self, context):
        context.criterions = self

    def check(self, context, **kwargs):
        self.check_list_of("criterions", context, **kwargs)


class SMECriterion(BaseTypeParent):

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    def set_data_to_context(self, context):
        context.criterion = self

    def __init__(self, data: dict):
        super().__init__()
        self.active = data.get("active")
        self.amount_check = data.get("amount_check")
        self.count_check = data.get("count_check")
        self.created_at = data.get("created_at")
        self.date_action = data.get("date_action")
        self.date_check = data.get("date_check")
        self.id = data.get("id")
        self.list_id = data.get("list_id")
        self.name = data.get("name")
        self.points = data.get("points")
        self.step_id = data.get("step_id")
        self.user_employee = data.get("user_employee")

    def check(self, context, **kwargs):
        self.assert_not_empty_bool("active")
        self.assert_not_empty_int("amount_check")
        self.assert_not_empty_numeric("count_check")
        self.assert_not_empty_str("created_at")
        self.assert_not_empty_numeric("date_action")
        self.assert_not_empty_numeric("date_check")
        self.assert_not_empty_str("id")
        self.assert_not_none_and_true_type("list_id", str)
        self.assert_not_empty_str("name")
        self.assert_not_empty_numeric("points")
        self.assert_not_empty_str("step_id")
        self.assert_not_empty_str("user_employee")
