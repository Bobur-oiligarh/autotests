import allure

from onboarding_physical.requests.internal.private_prospects_by_prospect_id_requests import PrivateProspectsByProspectID


@allure.step('Запрашиваем private_prospect по prospect_id и проверяем')
def step_private_prospect_by_prospect_id(context):
    response = PrivateProspectsByProspectID(context).response()
    response.check_success(context).data.set_data_to(context)
