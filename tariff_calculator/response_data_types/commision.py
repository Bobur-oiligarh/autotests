from utils.api_utils.response_data_base import BaseTypeParent


class Commission(BaseTypeParent):

    def __init__(self, data: dict):
        super().__init__()
        self.commission = data["commission"]
        self.otp = data["otp"]
        self.limit_day = data["limit_day"]
        self.limit_month = data["limit_month"]

    def set_data_to(self, obj):
        self.set_comm_to_context(obj)

    def set_comm_to_context(self, context):
        context.commission = self

    def check(self, context, **kwargs):
        self.assert_not_none("commission")
        self.assert_not_none("otp")
        self.assert_not_none("limit_day")
        self.assert_not_none("limit_month")
