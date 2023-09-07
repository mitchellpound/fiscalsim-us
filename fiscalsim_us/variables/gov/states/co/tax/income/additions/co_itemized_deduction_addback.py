from fiscalsim_us.model_api import *


class co_itemized_deduction_addback(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado federal itemized deduction addback"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        pass
