import allure

from utils.api_utils.response_data_base import BaseTypeParent, BaseType


class Cards(BaseTypeParent):

    def __init__(self, data: list):
        super().__init__()
        self.cards_list: list[Card] = self.deserialize_to_list_of(Card, data)

    def set_data_to(self, obj):
        self.set_data_to_context(obj)

    @allure.step("Установить карты в переменную контекста")
    def set_data_to_context(self, context):
        context.cards = self

    def check(self, client, **kwargs):
        self.check_all_cards()

    @allure.step("Проверка всех карт ответа")
    def check_all_cards(self, client, **kwargs):
        for card in self.cards_list:
            with allure.step(f"Проверка параметров карты {card.card_number}"):
                card.check(client, **kwargs)


class Card(BaseType):

    def __init__(self, data: dict):
        super().__init__()
        self.card_id = data["card_id"]
        self.card_number = data["card_number"]
        self.owner = data["owner"]
        self.balance = data["balance"]
        self.hold_amount = data["hold_amount"]
        self.state = data["state"]
        self.card_type = data["card_type"]
        self.processing = data["processing"]
        self.account = data["account"]
        self.expire = data["expire"]
        self.bank_code = data["bank_code"]

    def check(self, client, **kwargs):
        self.card_id_not_empty()
        self.card_number_not_empty()
        self.owner_not_empty()
        self.balance_not_null()
        self.hold_amount_not_null()
        self.state_not_empty()
        self.card_type_not_empty()
        self.processing_not_empty()
        self.account_not_empty()
        self.expire_not_empty()
        self.bank_code_not_null()

    @allure.step("cadr_id не пустой")
    def card_id_not_empty(self):
        self._tc.assertNotEqual(self.card_id, "",
                                f"card_id ({self.card_id}) пустой" + self.__str__())

    @allure.step("card_number не пустой")
    def card_number_not_empty(self):
        self._tc.assertNotEqual(self.card_number, "",
                                f"card_number ({self.card_number}) пустой" + self.__str__())

    @allure.step("owner не пустой")
    def owner_not_empty(self):
        self._tc.assertNotEqual(self.owner, "",
                                f"owner ({self.owner}) пустой" + self.__str__())

    @allure.step("balance не пустой")
    def balance_not_null(self):
        self._tc.assertIsNotNone(self.balance,
                                 f"balance ({self.balance}) пустой" + self.__str__())

    @allure.step("hold_amount не пустой")
    def hold_amount_not_null(self):
        self._tc.assertIsNotNone(self.hold_amount,
                                 f"hold_amount ({self.hold_amount}) пустой" + self.__str__())

    @allure.step("state не пустой")
    def state_not_empty(self):
        self._tc.assertNotEqual(self.state, "",
                                f"state ({self.state}) пустой" + self.__str__())

    @allure.step("card_type не пустой")
    def card_type_not_empty(self):
        self._tc.assertNotEqual(self.card_type, "",
                                f"card_type ({self.card_type}) пустой" + self.__str__())

    @allure.step("processing не пустой")
    def processing_not_empty(self):
        self._tc.assertNotEqual(self.processing, "",
                                f"processing ({self.processing}) пустой" + self.__str__())

    @allure.step("account не пустой")
    def account_not_empty(self):
        self._tc.assertNotEqual(self.account, "",
                                f"account ({self.account}) пустой" + self.__str__())

    @allure.step("expire не пустой")
    def expire_not_empty(self):
        self._tc.assertNotEqual(self.expire, "",
                                f"expire ({self.expire}) пустой" + self.__str__())

    @allure.step("bank_code не пустой")
    def bank_code_not_null(self):
        self._tc.assertIsNotNone(self.bank_code,
                                 f"bank_code ({self.bank_code}) пустой" + self.__str__())
