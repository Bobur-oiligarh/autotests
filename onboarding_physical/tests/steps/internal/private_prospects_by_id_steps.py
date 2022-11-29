import allure

from onboarding_physical.requests.internal.get_private_prospects_by_prospect_id import GetPrivateProspectsByProspectID


@allure.step('Запрашиваем private_prospect по prospect_id и проверяем')
def step_private_prospect_by_prospect_id(context):
    response = GetPrivateProspectsByProspectID(context).response()
    response.check_success(context).data.set_data_to(context)
