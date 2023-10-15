from fiscalsim_us.model_api import *


class co_pension_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado taxable pension subtractions from income"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.co.tax.subtractions
        # assume that the head of household is recieving the pension
        age = tax_unit("age_head", period)
        ss_subtract = tax_unit("co_social_security_subtraction", period)
        # currently assuming that spouse ss and taxable pension = 0
        # since the variables are not specific to head/ spouse
        taxable_pension = tax_unit("taxable_pension_income", period)
        # tax code only allows tax unit to subtract the max benefit between
        # both the ss and pension subtraction
        max_subtract = p.pension_max.calc(age) - ss_subtract
        return min_(taxable_pension, max_subtract)
