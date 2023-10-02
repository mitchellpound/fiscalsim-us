from fiscalsim_us.model_api import *


class co_pension_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado total subtractions from income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        pass
