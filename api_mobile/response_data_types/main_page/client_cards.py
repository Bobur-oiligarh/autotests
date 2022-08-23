import allure

from api_mobile.response_data_types.response_data_base import BaseType


class Cards(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.cards: list
        self._set_cards(data)
        self.total_sum = data["total_sum"]

    def _set_cards(self, data: dict):
        self.cards = []
        for value in data["cards"].values():
            self.cards.append(Card(value))

    def check(self, client, **kwargs):
        super().check(client, **kwargs)
        total_sum_uzs = 0.0
        for card in self.cards:
            with allure.step(f"проверка параметров карты {card.mask_num}"):
                card.check(client, **kwargs)
            total_sum_uzs += card.balance

    @allure.step("проверка наличия total_sum")
    def total_sum_not_null(self):
        self.tc.assertNotEqual(self.total_sum, "",
                               f"total_sum пустой")

    @allure.step("total_sum соответствует сумме балансов")
    def total_sum_is_true(self, expired_total_sum):
        self.tc.assertEqual(self.total_sum, expired_total_sum,
                            f"total_sum {self.total_sum} не соответствует "
                            f"сумме полученных карт {expired_total_sum}")


class Card(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.card_type = data["card_type"]
        self.mfo = data["mfo"]
        self.mask_num = data["mask_num"]
        self.state = data["state"]
        self.balance = data["balance"]
        self.ps_code = data["ps_code"]
        self.expire = data["expire"]
        self.owner = data["owner"]

    def check(self, client, **kwargs):
        self.card_id_not_empty()
        pass

    @allure.step("проверка наличия card_id")
    def card_id_not_empty(self):
        self.tc.assertNotEqual(self.card_id, "",
                               f"card_id пустой" + self.__str__())

    @allure.step("проверка наличия card_type")
    def card_type_not_empty(self):
        self.tc.assertNotEqual(self.card_type, "",
                               f"card_type пустой" + self.__str__())

    @allure.step("проверка наличия mfo")
    def mfo_not_empty(self):
        self.tc.assertNotEqual(self.mfo, "",
                               f"mfo пустой" + self.__str__())

    @allure.step("проверка наличия mask_num")
    def mask_num_not_empty(self):
        self.tc.assertNotEqual(self.mask_num, "",
                               f"mask_num пустой" + self.__str__())

    @allure.step("проверка наличия state")
    def state_not_empty(self):
        self.tc.assertNotEqual(self.state, "",
                               f"state пустой" + self.__str__())

    @allure.step("проверка наличия balance")
    def balance_not_none(self):
        self.tc.assertNotEqual(self.balance, None,
                               f"balance пустой" + self.__str__())

    @allure.step("проверка наличия ps_code")
    def ps_code_not_empty(self):
        self.tc.assertNotEqual(self.ps_code, "",
                               f"ps_code пустой" + self.__str__())

    @allure.step("проверка наличия expire")
    def expire_not_empty(self):
        self.tc.assertNotEqual(self.expire, "",
                               f"expire пустой" + self.__str__())

    @allure.step("проверка наличия owner")
    def owner_not_empty(self):
        self.tc.assertNotEqual(self.owner, "",
                               f"owner пустой" + self.__str__())
