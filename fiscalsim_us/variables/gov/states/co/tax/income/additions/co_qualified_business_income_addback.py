from fiscalsim_us.model_api import *


class co_qualified_business_income_addback(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado qualified business income addback "
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.co.tax.income.additions
        agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        itemizes = tax_unit("tax_unit_itemizes", period)
        business_income_deduct = tax_unit("qualified_business_income_deduction")

        required = agi > p.qualified_business_income_threshold[filing_status]
        # This variable does not include the addback for being in a
        # partnership that made a SALT Parity Election.

        return required * itemizes * business_income_deduct
