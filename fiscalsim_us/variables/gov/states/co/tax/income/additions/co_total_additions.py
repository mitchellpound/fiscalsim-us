from fiscalsim_us.model_api import *


class co_total_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado total additions to income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO
    adds = [
        "co_salt_addback",
        "co_qualified_business_income_addback",
        "co_itemized_deduciton_addback"
        "co_other_additions"
    ]
