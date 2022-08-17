import allure

from utils.methods import obj_to_string


class BaseType:
    def __str__(self):
        return obj_to_string(self)

    @allure.step("Проверка параметров ответа")
    def check(self, client):
        pass
