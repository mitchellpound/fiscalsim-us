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
       p = parameters(period).gov.states.co.tax.income.additions
       filing_status = tax_unit("filing_status", period)
       agi = tax_unit("adjusted_gross_income", period)

       itemizing = tax_unit("tax_unit_itemizes", period)
       itemized_deducts = tax_unit("taxable_income_deductions_if_itemizing", period)

       income_required = agi >= p.itemized_deduciton_addback_income_threshold[filing_status]
       deducts_required = itemized_deducts >= p.itemized_deduction_threshold[filing_status]

       where(
           income_required * deducts_required,
           itemized_deducts - p.itemized_deduction_addback_subtraction[filing_status],
           0
             )
