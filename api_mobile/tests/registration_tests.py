from api_mobile.requests.registration import StartRegistration, FinishRegistration, GetOffer
import unittest
import allure


@allure.story("Start registration")
class StartRegistrationTest(unittest.TestCase):

    @allure.step("Start registration")
    def startReg(self, client):
        response = StartRegistration(client).get_response()
        response.check()
        client.sign_id = response.data.sign_i
        print(client.sign_id)


@allure.story("Finish registration")
class FinishRegistrationTest(unittest.TestCase):

    @allure.step("Finish registration")
    def finishReg(self, client):
        response = FinishRegistration(client).get_response()
        response.check(client)
        client.access_token = response.data.access_token
        client.refresh_token = response.data.refresh_token


class GetOfferTest(unittest.TestCase):

    @allure.step("Get Offer")
    def getOffer(self, client):
        response = GetOffer(client).get_response()
        response.check()
