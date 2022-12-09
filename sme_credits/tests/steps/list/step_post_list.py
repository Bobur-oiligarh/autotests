import allure

from sme_credits.requests.list.post_list import PostList


@allure.step("Запрос Post/list, проверка ответа")
def step_post_list(context):
    response = PostList(context).response()
    response.check_success(context).data.set_data_to(context)
