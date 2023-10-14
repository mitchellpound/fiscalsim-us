from fiscalsim_us.model_api import *


class co_total_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado total subtractions from income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
    adds = [
        # state income tax refund line 1 Schedule 1 Form 1040
        "us_govt_interest",
        "co_social_security_subtraction",
        "co_pension_subtraction",
        "co_other_subtractions"
    ]
