import allure

from onboarding_physical.requests.internal.get_private_address_by_address_id import \
    GetPrivateAddressByAddressID


@allure.step('Запрашиваем адрес по address_id и проверяем')
def step_private_address_by_id(context):
    response = GetPrivateAddressByAddressID(context).response()
    response.check_success(context).data.set_data_to(context)
