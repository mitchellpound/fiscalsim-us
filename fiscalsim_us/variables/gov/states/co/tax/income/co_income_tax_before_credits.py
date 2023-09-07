
from fiscalsim_us.model_api import *


class co_income_tax_before_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado income tax before credits"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
