import allure

from onboarding_physical.requests.internal.put_private_address_by_prospect_id import PutPrivateAddressRequest
from onboarding_physical.test_data.onboarding_physical_context import OnboardingPhysicalContext


@allure.step('Делаем put запрос и проверяем ответ')
def step_put_private_address_to_prospect(context: OnboardingPhysicalContext):
    response = PutPrivateAddressRequest(context).response()
    response.check_success(context)

