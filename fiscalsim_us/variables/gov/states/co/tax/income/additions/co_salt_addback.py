from fiscalsim_us.model_api import *


class co_salt_addback(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado state and local taxes deduciton addback"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
