from fiscalsim_us.model_api import *


class co_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
    adds = ["co_income_tax_before_credits"]
    subtracts = ["co_nonrefundable_credits"]
