from fiscalsim_us.model_api import *


class co_other_subtractions(Variable):
    """
    Colorado other subtractions from income. These include:
    - Military Retirement Subtraction
    - Colorado Agricultural Land Capital Gain Subtraction
    - CollegeInvest Contribution
    - Qualified Reservation Income
    - PERA/DPSRS Subtraction
    - Railroad Benefit
    - Wildfire Mitigation Measures
    - Colorado Marijuana Business Deduction
    - Non-Resident Disaster Relief Worker Subtraction
    - Reacquisition of Colorado Residency During Active Duty Military
        Service Subtraction
    - First Time Home Buyer Savings Account Interest Deduction
    - Carryforward Subtractions Allowed Under HB21-1002
    """
    value_type = float
    entity = TaxUnit
    label = "Colorado other subtractions from income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
