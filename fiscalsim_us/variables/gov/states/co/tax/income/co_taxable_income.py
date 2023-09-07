from fiscalsim_us.model_api import *


class co_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado taxable income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
    adds = ["adjusted_gross_income", "co_total_additions"]
    subtracts = ["co_total_subtractions"]
