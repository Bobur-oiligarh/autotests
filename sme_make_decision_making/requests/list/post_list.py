from sme_make_decision_making.response_data_types.lists import SMEList
from utils.api_utils.test_request import TestRequest
from utils.url_provider import URLProvider


class PostList(TestRequest):
    """У объекта list нет поле с автоинкремент (как id),
    поэтому перед созданием нужно убедиться что в БД нет объекта с такими параметрами, иначе тесты упадут. """

    def __init__(self, context):
        super().__init__(
            url=URLProvider().url("sme_make_decision_making", "list"),
            method="post",
            data_type=SMEList,
            require_err_note=False
        )
        self.list_id = context.list.list_id
        self.name = context.list.name
        self.user_employee = context.list.user_employee
        self.active = context.list.active
